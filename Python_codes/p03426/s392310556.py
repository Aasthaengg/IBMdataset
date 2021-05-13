h,w,d = map(int,input().split())
p = [(0,0)] * (h*w)
c = [0] * (h*w)
for i in range(h):
  a = list(map(int,input().split()))
  for j in range(w):
    p[a[j]-1] = (i,j)

for i in range(d, h*w):
  c[i] = c[i-d] + abs(p[i][0] - p[i-d][0]) + abs(p[i][1] - p[i-d][1])

q = int(input())
ans = 0
for i in range(q):
  l,r = map(int,input().split())
  print(c[r-1] - c[l-1])