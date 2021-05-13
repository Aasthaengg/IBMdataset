from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

A = [a - 1 for a in A]
Acum = [0]
for a in A:
  Acum.append((Acum[-1] + a) % K)

answer = 0
counter = defaultdict(int)
for i, ai in enumerate(Acum):
  answer += counter[ai]
  counter[ai] += 1
  if i - K + 1 >= 0:
    counter[Acum[i - K + 1]] -= 1
    
print(answer)