a, b = map(int, input().split())
c = int(str(a)+str(b))
ans = 'No'

n = 0
while True:
  n += 1
  if c == n**2:
    ans = 'Yes'
  if n**2 > c:
    break

print(ans)