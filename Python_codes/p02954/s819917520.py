s=input()
n=len(s)
ans=[0 for i in range(n)]
r=0
l=0

for i in range(n):
  if s[i]=="R":
    r+=1
  else:
    plus=r//2
    ans[i]+=plus
    ans[i-1]+=(r-plus)
    r=0

for i in range(n-1,-1,-1):
  if s[i]=="L":
    l+=1
  else:
    plus=l//2
    ans[i]+=plus
    ans[i+1]+=l-plus
    l=0
print(*ans)