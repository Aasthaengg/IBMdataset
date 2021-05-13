N = int(input())
M = 26
n = 0
m = 1
s = [0, 0]
while s[1] < N:
  m *= M
  s[0] = s[1]
  s[1] += m
  n += 1
N = N - s[0] - 1
ans = ""
for i in range(n):
  ans = chr(ord("a") + (N % M)) + ans
  N //= M
print(ans)