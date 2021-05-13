a,b,c = map(int,input().split())
ans = b
ans += min(c,b)
c = max(0,c-b)
if a>=c:
  ans+=c
else:
  ans+=a+1
print(ans)
