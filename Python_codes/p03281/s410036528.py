N = int(input())

def num_p(n):
  r = 0
  for i in range(1,n+1):
    if n % i == 0:
      r += 1
  return r

ans = 0
for i in range(1, N+1, 2):
  if num_p(i) == 8:
    ans += 1
print(ans)
