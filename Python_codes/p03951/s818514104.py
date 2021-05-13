n=int(input())
s=str(input())
t=str(input())
s=list(s)
t=list(t)
ans=2*n
for i in range(n):
  cnt=0
  for j in range(n-i):
    if s[i+j]!=t[j]:
      break
    else:
      cnt=cnt+1
  if cnt==n-i:
    ans=ans-n+i
    break
print(ans)