def resolve():
    N = int(input())
    A = input()
    B = input()
    C = input()
    ans = 0
    for i in range(N):
        if A[i] != B[i] != C[i] != A[i]:
            ans += 2
        elif A[i] == B[i] == C[i]:
            ans += 0
        else:
            ans += 1
    print(ans)
resolve()