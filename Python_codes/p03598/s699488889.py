n = int(input())
k = int(input())
ans = 0
for x in map(int, input().split()):
  ans += min(x, abs(k - x)) * 2
print(ans)