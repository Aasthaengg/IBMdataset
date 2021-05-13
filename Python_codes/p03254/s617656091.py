n, x = map(int, input().split())
a = [int(an) for an in input().split()]
a.sort()
ans = 0
num_candy = 0
for an in a:
  num_candy += an
  if num_candy <= x:
    ans += 1
if num_candy < x:
  ans -= 1
print(ans)