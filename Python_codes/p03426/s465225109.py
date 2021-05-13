h,w,d = map(int,input().split())

dic = {}
for i in range(h):
  line = list(map(int,input().split()))
  for j in range(w):    
    dic[line[j]-1]=(i,j)              

A = [0]*(h*w)

for i in range(h*w-d):
    x,y = dic[i]
    nx,ny = dic[i+d]      
    A[i+d] = A[i] + abs(nx-x) + abs(ny-y)
  
q = int(input())  
for i in range(q):
  l,r = map(int,input().split())
  print(A[r-1] - A[l-1])  