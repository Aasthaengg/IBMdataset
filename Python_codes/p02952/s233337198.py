N = int(input())

def cnt_keta(n):
  keta = 0
  while n > 0:
    n //= 10
    keta += 1
  return keta

ans = 0
for i in range(1, N+1):
  if cnt_keta(i) % 2 == 1:
    ans += 1
print(ans)