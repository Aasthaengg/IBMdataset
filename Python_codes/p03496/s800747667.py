N = int(input())
As = list(map(int, input().split()))
rs = []
n = max(range(N), key=lambda i: abs(As[i]))
for i in range(N):
  rs.append((n, i))
if As[n] > 0:
  for i in range(1, N):
      rs.append((i-1, i))
if As[n] < 0:
  for i in reversed(range(1, N)):
      rs.append((i, i-1))
#print(rs)
print(len(rs))
for x, y in rs:
  print(x+1, y+1)
