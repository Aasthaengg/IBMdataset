A, B, K = map(int, input().split())

L = []

for i in range(A, min(A+K, B+1)):
  L.append(i)
for i in range(B, max(B-K, A-1), -1):
  L.append(i)

ans = sorted(set(L))

print(*ans, sep="\n")