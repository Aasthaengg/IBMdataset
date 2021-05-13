n = int(input())
v = list(map(int, input().split()))
v = sorted(v)
while len(v) != 1:
  v[1] = (v[0]+v[1])/2
  v = sorted(v[1:])
print(*v)