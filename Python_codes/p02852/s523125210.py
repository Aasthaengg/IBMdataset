N, M = map(int, input().split())
S = input().strip()
T = S[::-1]

l = []
i = 0
while i < N:
  t = T[i+1: i+M+1][::-1]
  if '0' not in t:
    print(-1)
    exit()
  else:
    x = min(M - t.index('0'), len(t))
    l.append(x)
    i += x
print(*l[::-1])