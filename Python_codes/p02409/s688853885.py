count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

n = int(input())


b_list=[]
f_list=[]
r_list=[]
v_list=[]
while n > 0:
  b, f, r, v = map(int, input().split())
  b_list.append(b)
  f_list.append(f)
  r_list.append(r)
  v_list.append(v)
  n = n-1

for (blist,flist,rlist,vlist) in zip(b_list,f_list,r_list,v_list):
  count[blist-1][flist-1][rlist-1] = count[blist-1][flist-1][rlist-1] + vlist

for i in range(0, 4):
  for j in range(0, 3):
    for k in range(0, 10):
      print("",count[i][j][k],end="")
    print()
  if i != 3:
    print("####################")
