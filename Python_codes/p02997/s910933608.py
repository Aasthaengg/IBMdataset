import itertools

n,k = map(int, input().split())
if k > (n-1) * (n-2) // 2:
  print(-1)
  exit()
m = n * (n-1) // 2 - k
print(m)
for i in range(1,n):
  print(i,n)
add = (n-1) * (n-2) // 2 - k
for i in itertools.combinations(range(1,n),2):
  if not add:
    break
  print(*i)
  add -= 1