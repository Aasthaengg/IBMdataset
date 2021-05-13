n=int(input())
p=[int(input()) for _ in range(n)]
s=set()
for i in p:
  if i-1 in s:s-={i-1}
  s|={i}
s=[0]+sorted(list(s))
ans=n
for i in range(len(s)-1):
  ans=min(ans,n-s[i+1]+s[i])
print(ans)