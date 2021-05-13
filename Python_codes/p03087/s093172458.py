n,q=map(int, input().split())
s=input()
cnt=[0]*(n-1)
for i in range(n-1):
  if s[i:i+2]=='AC':
    cnt[i]=1
cnt2=[0]*(n)
for i in range(1,n):
  cnt2[i]=cnt2[i-1]+cnt[i-1]
for i in range(q):
  l,r=map(int, input().split())
  print(cnt2[r-1]-cnt2[l-1])