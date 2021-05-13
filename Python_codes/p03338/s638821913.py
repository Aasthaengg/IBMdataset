N = int(input())
S = input()
C = [chr(i) for i in range(97, 123)]
ans = 0
for i in range(0, N - 1):
  count = 0
  a = S[:i + 1]
  b = S[i + 1:]
  for c in C:
    if c in a and c in b:
      count += 1
  ans = max(count, ans)
print(ans)