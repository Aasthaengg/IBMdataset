N, M = map(int,input().split())
A=list(map(int, input().split()))
for i in A:
    if sum(A) > N:
        ans = -1
    else:
        ans = N - sum(A)
print(ans)