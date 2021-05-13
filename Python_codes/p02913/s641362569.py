def z_algo(S):
    N = len(S)
    A = [0] * N
    i = 1
    j = 0
    A[0] = l = len(S)
    while i < l:
        while i + j < l and S[j] == S[i + j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l-i > k < j - A[k]:
            A[i + k] = A[k]
            k += 1
        i += k
        j -= k
    return A


def resolve():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        a = z_algo(s[i:])
        for index, j in enumerate(a):
            if j <= index:
                ans = max(ans, j)
    print(ans)


if __name__ == '__main__':
    resolve()
