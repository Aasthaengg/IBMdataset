p,q,r = map(int,input().split())
ans = 0
if p>=q and p>=r:
  ans += q + r
elif q>=p and q>=r:
  ans += p + r
elif r>=p and r>=q:
  ans += p + q

print(ans)