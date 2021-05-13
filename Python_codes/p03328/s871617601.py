A, B = map(int, input().split())
h = B-A
ans = 0
for i in range(1, h):
  ans += i
print(ans-A)