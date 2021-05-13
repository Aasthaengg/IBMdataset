def resolve():
    n = int(input())
    A = [int(i) for i in input().split()]
    ans = [False] * 2001
    for i in range(2**n):
        sumA = 0
        for j in range(n):
            if (i >> j) & 1:
                sumA += A[j]
        ans[sumA] = True
    q = int(input())
    M = [int(i) for i in input().split()]
    for m in M:
        if ans[m]:
            print("yes")
        else:
            print("no")


resolve()

