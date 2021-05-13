def z_algorithm(S):
    n = len(S)
    A = [0] * n
    A[0] = n
    L = 0
    R = 0
    # 過去にS[R]まで調べたとする
    for i in range(1, n):
        if R <= i:
            L = R = i
            while R < n and S[R] == S[R - L]:
                R += 1
            A[i] = R - L
        elif A[i - L] < R - i:
            A[i] = A[i - L]
        else:
            L = i
            while R < n and S[R] == S[R - L]:
                R += 1
            A[i] = R - L
    return A


def main():
    N = int(input())
    S = input()
    answer = 0
    for i in range(N):
        a = z_algorithm(S[i:])
        for j in range(1, N - i):
            cnt = min(j, a[j])
            if cnt > answer:
                answer = cnt

    print(answer)


if __name__ == '__main__':
    main()
