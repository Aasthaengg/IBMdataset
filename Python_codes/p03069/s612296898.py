N = int(input())
S = list(input())
a = 0
b = 0
A = []
for i in range(N):
  if S[i] == '.':
    a += 1
  else:
    b += 1
  A.append(b-a)
A.sort()
ans = min(a, b, a+A[0])
print(ans)