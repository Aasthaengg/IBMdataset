n=int(input())
s=list(input())
ans=0
for i in range(n-1):
  ans=max(ans,len(set(s[:i+1]))+len(set(s[i+1:]))-len(set(s)))
print(ans)