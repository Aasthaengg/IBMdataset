A, B, K = list(map(lambda x: int(x), input().split(" ")))
ans = []
for i in range(A, min([A + K, B + 1])):
  ans.append(i)
for j in range(max([B - K + 1, A]), B + 1):
  ans.append(j)

ans = list(set(ans))
ans.sort()

print("\n".join(list(map(lambda s: str(s), ans))))