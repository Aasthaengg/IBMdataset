N,A,B = map(int,input().split())
lsX = list(map(int,input().split()))
ans = 0
for i in range(1,N):
    ans += min((lsX[i] - lsX[i-1])*A, B)
print(ans)