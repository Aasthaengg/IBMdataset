N,M = map(int,input().split())
AList = list(map(int,input().split()))
AList.sort(reverse=True)
NList=[0,2,5,5,4,5,6,3,7,6]
CList=[]
minnum = (-1)*(10**10)
dp = [0]*(N+1)

for a in AList:
    u = NList[a]
    if (u in CList) == False:
        CList.append(u)

dp[0] = 0
for n in range(1,N+1):
    max1 = minnum
    for c in CList:
        if c <= n:
            if dp[n-c] == minnum:
                num = minnum
            else:
                num = dp[n-c]+1
            if max1 < num:
                max1 = num
    dp[n] = max1
keta = dp[N]
s = ''
nn = N
for n in range(keta):
    for a in AList:
        if nn >= NList[a] and dp[nn-NList[a]] == dp[nn]-1:
            s += str(a)
            nn -= NList[a]
            break
print(s)
