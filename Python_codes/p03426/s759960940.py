h,w,d = tuple(map(int,input().split()))

a = [[int(t)for t in input().split()]for _ in [0]*h]

pos = [0]*(h*w)

for i in range(h):
  for j in range(w):
    pos[a[i][j]-1] = (i,j)

cusum = [0]*d


for i in range(h*w-d):
  x,y = pos[i]
  z,w = pos[i+d]
  cost = abs(x-z)+abs(y-w)
  cusum.append(cusum[-d]+cost)

q = int(input())

for i in range(q):
  l,r = tuple(map(int,input().split()))
  l,r = l-1,r-1
  print(cusum[r]-cusum[l])