n,m=map(int,input().split())
s,l=input(),[]
while n>0:
 for i in range(m,0,-1):
  if i<=n and s[n-i]=="0":l.append(i);n-=i;break
 else:exit(print(-1))
print(*l[::-1])