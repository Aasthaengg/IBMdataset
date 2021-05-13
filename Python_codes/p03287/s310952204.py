N, M = list(map(int, input().split()))

D = list(map(int, input().split()))

S = {0 : 1}
t = 0
for i in range(N):
  t = (t + D[i]) % M
  if t in S:
    S[t] += 1
  else:
    S[t] = 1

r = 0

for i in S.values():
  r += i * (i - 1) // 2
  
print(r)