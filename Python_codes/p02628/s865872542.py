N, K = map(int, input().split())
p = [int(e) for e in input().split()]

# print(p)
p.sort()
# print(p)

ans = 0
for e in p[:K]:
  ans += e

print(ans)
