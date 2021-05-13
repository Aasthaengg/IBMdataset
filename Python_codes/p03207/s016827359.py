n = int(input())
p = list()
for _ in range(n):
  p.append(int(input()))
p.sort()
ans = sum(p)
ans -= p[-1]//2
print(ans)