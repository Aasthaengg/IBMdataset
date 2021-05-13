n,k=map(int,input().split())
s=input()
u=s.count('RL')
if u>k:
  print(n-(u-k)*2-(s[0]=='L')-(s[n-1]=='R'))
else:
  print(n-1-(s[0]=='L')*(s[n-1]=='R')*(u==k))