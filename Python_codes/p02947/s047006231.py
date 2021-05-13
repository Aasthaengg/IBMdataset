n = int(input())
xs = [''.join(sorted(list(input()))) for _ in range(n)]

mem = {}
ans = 0
for s in xs:
  if s in mem:
    ans += mem[s]
    mem[s] += 1
  else:
    mem[s] = 1
print(ans)
