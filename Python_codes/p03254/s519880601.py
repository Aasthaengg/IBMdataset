N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0

if X > sum(A):
    print(N-1)
else:
    for i in range(len(A)):
        if X >= A[i]:
            X -= A[i]
            ans += 1
        else:
            break
    print(ans)
