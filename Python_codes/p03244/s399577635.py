n=int(input())
v=list(map(int,input().split()))
a=n//2
dp=[[0,0]for i in range(10**5+1)]
bp=[[0,0]for i in range(10**5+1)]
for i in range(n):
  if i%2==0:
    dp[v[i]][0]+=1
    dp[v[i]][1]=v[i]
  else:
    bp[v[i]][0]+=1
    bp[v[i]][1]=v[i]
dp.sort(reverse=True)
bp.sort(reverse=True)
if bp[0][1]==dp[0][1]:
  if dp[1][0]>=bp[1][0]:
    dp[0][0]=dp[1][0]
  else:
    bp[0][0]=bp[1][0]
print(a-dp[0][0]+a-bp[0][0])