def calc_dist(pos_a,pos_b):
  return abs(pos_a[0] - pos_b[0])+abs(pos_a[1] - pos_b[1])

n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
  a.append(list(map(int,input().split())))
for i in range(m):
  b.append(list(map(int,input().split())))

for a_pos in a:
  min_d=float("inf")
  min_d_i=-1
  for i,b_pos in enumerate(b):
    d=calc_dist(a_pos,b_pos)
    if d < min_d:
      min_d=d
      min_d_i=i+1
  print(min_d_i)