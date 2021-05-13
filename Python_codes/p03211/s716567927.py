s=list(input())
n=len(s)
s=list(map(int,s))
ans=float("INF")
for i in range(n-2):
  ans=min(ans,abs(s[i]*100+s[i+1]*10+s[i+2]-753))
print(ans)
