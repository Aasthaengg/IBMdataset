N,x = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for i in range(1,N):
    y = max(A[i]+A[i-1]-x,0)
    if A[i]>=y:
        A[i] -= y
    else:
        A[i] = 0
    ans += y
print(ans)        