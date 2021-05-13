input()
A = list(input())
B = list(input())
C = list(input())

ans = 0
for a, b, c in zip(A, B, C):
  if a == b == c:
    ans += 0
  elif a == b or b == c or c == a:
    ans += 1
  else:
    ans += 2
print(ans)