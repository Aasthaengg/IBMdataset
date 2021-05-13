n = int(input())
a = list(map(int, input().split()))

odd, eve = 0, 0
for x in a:
  if x&1: odd += 1
  else: eve += 1
print("YES" if odd%2 == 0 else "NO")