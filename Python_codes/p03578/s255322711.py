N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
d = {}
for a in A:
  d[a] = d.get(a, 0) + 1
f = 0
for b in B:
  d[b] = d.get(b, 0) - 1
  if d[b] < 0:
    print("NO")
    f = 1
    break
if f == 0:
  print("YES")