N = int(input())
A = list(map(int,input().split()))
CSum=[[0 for i in range(N+1)] for j in range(21)]

for i in range(1,N+1):
    nowA = A[i-1]
    for j in range(21):
        CSum[j][i] = CSum[j][i-1]
        CSum[j][i] += nowA%2
        nowA //= 2

l = 0
r = 1
ans = 0
while r <= N :
    ok = True
    for i in range(21):
        if CSum[i][r] - CSum[i][l] >= 2:
            ok = False
    
    if ok:
        ans += r-l
        r += 1
    else:
        l += 1

print(ans)
