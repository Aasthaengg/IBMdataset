N = int(input())
t = []
for _ in range(N):
  a, b = map(int, input().split())
  t.append((a, b))
  
t.sort(key = lambda t: t[0] + t[1])
s = 0
while t:
  s += t.pop()[0]
  if t:
    s -= t.pop()[1]
    
print(s)