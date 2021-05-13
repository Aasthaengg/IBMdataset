import sys;sys.setrecursionlimit(9**9);h,w=map(int,input().split());b=[[0]*(w+1)]
for i in range(h):
  b.append([0])
  for j in input():b[-1].append(1+(j=="#"))
  b[-1].append(0)
b.append([0]*(w+1));d=[[0,1],[0,-1],[1,0],[-1,0]];a=0
def s(i,j):
  global B;B[b[i][j]-1]+=1;v=b[i][j];b[i][j]=0
  for k in d:
    if v^3==b[i+k[0]][j+k[1]]:s(i+k[0],j+k[1])
for i in range(1,h+1):
  for j in range(1,w+1):B=[0,0];s(i,j);a+=B[0]*B[1]
print(a)