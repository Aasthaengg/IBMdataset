from collections import defaultdict
D1 = defaultdict(int)

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
  D1[i] += 1

for _ in range(M):
  B, C = map(int, input().split())
  D1[C] += B

D2 = sorted(D1.items(), reverse=True)

ans = 0
temp = N

for i in range(len(D2)):
  if temp <= D2[i][1]:
    ans += D2[i][0] * temp
    break
  else:
    ans += D2[i][0] * D2[i][1]
    temp -= D2[i][1]

print(ans)