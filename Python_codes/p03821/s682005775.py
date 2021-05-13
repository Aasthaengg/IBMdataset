N = int(input())
AB = [0] * N
for n in range(N):
  AB[-1-n] = [int(x) for x in input().strip().split()]
ans = 0
cnt = 0
for (a, b) in AB:
  mod = (a + cnt) % b
  if mod:
    t = b - mod
    cnt += t
    ans += t
print(ans)
