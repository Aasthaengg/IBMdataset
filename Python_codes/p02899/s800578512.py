n = int(input())
m = [(x, 0) for x in range(1, n+1)]

for i, x in enumerate(map(int, input().split())):
  m[i] = (m[i][0], x)
m.sort(key=lambda x : x[1])
print(' '.join([str(x[0]) for x in m]))