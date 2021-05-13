N,K = map(int, input().split())
ans = 0
nusuke = [0] * N
for i in range(K):
  d = int(input())
  data = list(map(int, input().split()))
  for j in data:
    nusuke[j-1] += 1

for k in nusuke:
  if k == 0:
    ans += 1

print(ans)  