import math

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for a, b in AB[::-1]:
  if (a+ans)%b == 0:
    continue
  if a+ans >= b:
    ans += math.ceil(abs(a+ans)/b)*b-a-ans
  else:
    ans += b-a-ans
print(ans)