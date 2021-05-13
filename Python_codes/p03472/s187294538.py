N, H = map(int, input().split())

w = []
for i in range(N):
  a, b = map(int, input().split())
  w.append((a, 0))
  w.append((b, 1))

w.sort(reverse=True)
ans = 0
for v, t in w:
  if t == 1:
    H -= v
    ans += 1
  else:
    ans += -(-H//v)
    H = 0
  
  if H <= 0:
    break

print(ans)