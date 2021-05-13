bldgs = [[[0]*10 for _ in range(3)] for _ in range(4)]

n = int(input())
for _ in range(n):
  b, f, r, v = (int(i) for i in input().split())
  bldgs[b - 1][f - 1][r - 1] += v

for i, floors in enumerate(bldgs):
  if i != 0: print ("####################")
  for rooms in floors:
    print ("", *rooms)