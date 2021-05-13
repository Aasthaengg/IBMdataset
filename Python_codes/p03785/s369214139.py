n,c,k = map(int,input().split())
t = [int(input()) for nesya in range(n)]
t.sort()
bus = 0
wait = []
for i in range(n):
  wait.append(t[i])
  if wait[0] + k < t[i]:
    bus += 1
    wait = [t[i]]
  elif len(wait) == c:
    bus += 1
    wait = []
  elif wait[0] + k == t[i]:
    bus += 1
    wait = []
  if i == n-1 and len(wait) > 0:
    bus += 1
print(bus)