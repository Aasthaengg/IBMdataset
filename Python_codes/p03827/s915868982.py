N = int(input())
S = input()
x = 0
ans = 0
for s in S:
  x += 1 if s == "I" else -1
  ans = max(ans, x)
print(ans)