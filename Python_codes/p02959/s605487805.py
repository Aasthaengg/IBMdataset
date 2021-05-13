n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
rest = 0
for a, b in zip(B, A):
  b_ = b - rest
  if b_ > a:
    ans += rest + a
    rest = 0
  elif b_ > 0:
    rest = a - b_
    ans += b
  elif b_ <= 0:
    rest = a
    ans += b
b = A[-1]
if rest > b:
  ans += b
else:
  ans += rest
print(ans)