n,m=map(int, input().split())
a_list=[]
b_list=[]
for i in range(n):
  a,b=map(int, input().split())
  a_list.append(a)
  b_list.append(b)
c_list=[]
d_list=[]
for i in range(m):
  c,d=map(int, input().split())
  c_list.append(c)
  d_list.append(d)
for i in range(n):
  min=2*(10**8)
  min_number=0
  for j in range(m):
    d=abs(a_list[i]-c_list[j])+abs(b_list[i]-d_list[j])
    if d<min:
      min=d
      min_number=j
  print(min_number+1)
