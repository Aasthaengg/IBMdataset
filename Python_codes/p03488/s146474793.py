s=input()
x,y=map(int,input().split())
ss=[len(i) for i in s.split("T")]
x-=ss[0]
a=[]
b=[]
for i in range(1,len(ss)):
  if ss[i]==0:continue
  if i%2==1:b.append(ss[i])
  else:a.append(ss[i])
x=abs(x)
y=abs(y)
if max(x,y)>8000:exit(print("No"))
def check(n,a):
  dp=[[0]*20001 for _ in range(len(a)+1)]
  n+=10000
  dp[0][10000]=1
  for i in range(1,len(a)+1):
    for j in range(20001):
      if j+a[i-1]<=20000:dp[i][j+a[i-1]]|=dp[i-1][j]
      if j-a[i-1]>=0:dp[i][j-a[i-1]]|=dp[i-1][j]
  if dp[len(a)][n]==1:return True
  return False
if check(x,a) and check(y,b):print("Yes")
else:print("No") 
