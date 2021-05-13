a,b,x = map(int,input().split())
ans = 0
ad = a//x*x
bd = b//x*x
if ad == a:
  ans += 1
ans += (bd - ad) // x
print(ans)