n = int(input())
vlst = list(map(int, input().split()))
vlst.sort()
ans = vlst[0]
for v in vlst[1:]:
  ans = (ans + v) / 2
print(ans)