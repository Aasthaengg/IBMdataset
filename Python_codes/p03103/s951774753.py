N, M = map(int, input().split())
AB = []
for i in range(N):
  a, b = map(int, input().split())
  AB.append([a, b])

ans = 0
for ab in sorted(AB, key=lambda x: x[0]):
  if M >= ab[1]:
    ans += ab[0] * ab[1]
    M -= ab[1]
  else:
    ans += ab[0] * M
    M = 0
  if M <= 0:
    break

print(ans)