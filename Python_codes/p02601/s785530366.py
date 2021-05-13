a, b, c = map(int, input().split())
k = int(input())
ans = 'Yes'
for _ in range(k):
  if a >= b:
    b = 2*b
    k -= 1
    if b > a:
      break
k_2 = k
for _ in range(k_2):
  if b >= c:
    c = 2*c
if not a < b < c:
  ans = 'No'
print(ans) 