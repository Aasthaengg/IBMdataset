def main():
    _ = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 1e10)
    ans = []
    B = [0] * len(A)
    for i in range(len(A)-1, 0, -1):
        idx = i
        s = 0
        while idx <= len(A) - 1:
            s += B[idx]
            idx += i

        if s % 2 != A[i]:
            ans.append(i)
            B[i] = 1

    if len(ans) > 0:
        print(len(ans))
        print(*ans)
    else:
        print(0)


if __name__ == '__main__':
    main()
