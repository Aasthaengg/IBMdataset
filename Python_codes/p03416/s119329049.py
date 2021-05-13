A, B = map(int, input().split())
ans = 0

for i in range(A, B+1):
  a = str(i)
  b = ''.join(list(reversed(a)))
  if a == b:
    ans += 1

print(ans)