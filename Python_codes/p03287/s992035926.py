N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0]
for a in A:
  B.append((B[-1] + a) % M)

ans = 0
d = {}
for b in B:
  if b in d:
    ans += d[b]
    d[b] += 1
  else:
    d[b] = 1

print(ans)