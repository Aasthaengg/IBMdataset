n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
dp[0]=a[0]
for i in range(1,n):
  dp[i]=dp[i-1]+a[i]
ans1,ans2,cnt1,cnt2,flag=0,0,0,0,True
for i in range(n):
  if flag==True:
    if dp[i]+cnt1<=0:
      ans1+=abs(1-(dp[i]+cnt1))
      cnt1+=1-(dp[i]+cnt1)
    flag=False
  else:
    if dp[i]+cnt1>=0:
      ans1+=abs(-1-(dp[i]+cnt1))
      cnt1+=-1-(dp[i]+cnt1)
    flag=True

flag=False
for i in range(n):
  if flag==True:
    if dp[i]+cnt2<=0:
      ans2+=abs(1-(dp[i]+cnt2))
      cnt2+=1-(dp[i]+cnt2)
    flag=False
  else:
    if dp[i]+cnt2>=0:
      ans2+=abs(-1-(dp[i]+cnt2))
      cnt2+=-1-(dp[i]+cnt2)
    flag=True
print(min(ans1,ans2))