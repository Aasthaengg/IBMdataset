a = list(map(int,input().split()))
ans = sum(a)
if ans >= 22:
  ans = "bust"
else:
  ans = "win"
print(ans)