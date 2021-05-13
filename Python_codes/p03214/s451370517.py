n=int(input())
a=list(map(int,input().split()))
ave=sum(a)/n
m=10**10
ans=0
for i in a:
  if m>abs(ave-i):
    m=abs(ave-i)
    ans=i
print(a.index(ans))
