N = int(input())
p = list(map(int, input().split()))
ans = 0
q = []
for i in range(N):
  if i+1 == p[i]:
    q += [0]
  else:
    q += [1]

for i in range(N):
  if q[i] == 0 and i < N-1:
    q[i], q[i+1] = 1, 1
    ans += 1
  elif q[i] == 0 and i == N-1:
    q[i], q[i-1] = 1, 1
    ans += 1

print(ans)