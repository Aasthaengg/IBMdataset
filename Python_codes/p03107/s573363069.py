S = list(input())
N = len(S)
a = 0
b = 0
for i in range(N):
  if S[i] == '0':
    a += 1
  else:
    b += 1
m = min(a, b)
ans = 2 * m
print(ans)