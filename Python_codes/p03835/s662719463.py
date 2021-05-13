import itertools
k,s = map(int,input().split())

cnt = 0

for i in range(0,k+1):
  for j in range(0,k+1):
    z = s - i -j
    if z >= 0 and z <= k:
      cnt += 1

print(cnt)
