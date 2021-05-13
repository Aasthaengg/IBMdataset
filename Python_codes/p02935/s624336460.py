n = int(input())
v = list(map(int, input().split( )))
v1 = sorted(v)
for _ in range(n-1):
  new = (v1[0] + v1[1])/2
  v1 = v1[2:]
  v1.append(new)
  v1 = sorted(v1)
print(v1[0])