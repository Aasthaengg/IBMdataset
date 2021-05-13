n=int(input())
m=1
a=[]
while n>26:
  n,mod=divmod(n,26)
  if mod==0:
    mod==26
    n-=1
  a.append(mod)
  m+=1
a.append(n)
s="abcdefghijklmnopqrstuvwxyz"
ans=""
for i in range(m-1,-1,-1):
  ans+=s[a[i]-1]
print(ans)