h,w,z = map(int,input().split())
a_mat = []
for i in range(h):
  a_list = list(map(int,input().split()))
  a_mat.append(a_list)
pos_dic  = {}
for i in range(h):
  for j in range(w):
    pos_dic[a_mat[i][j] - 1] = [i,j]
    
d = [0 for i in range(h*w)]
for a in range(z,h*w):
  d[a] = d[a-z] + abs(pos_dic[a][0] - pos_dic[a-z][0]) +abs(pos_dic[a][1] - pos_dic[a-z][1])
  
q = int(input())
for _ in range(q):
  l,r = map(int,input().split())
  print(d[r-1] - d[l-1])
 
    
