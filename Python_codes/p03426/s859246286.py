h,w,d = map(int,input().split())

dic = {}
for i in range(h):
  line = list(map(int,input().split()))
  for j in range(w):    
    dic[line[j]-1]=(i,j)              

q = int(input())
L = [0]*q
R = [0]*q    
    
for i in range(q):
  L[i],R[i] = map(int,input().split())    
    
A = [0]*(h*w)
i = 0
j = 0
while i < h*w:  
  if A[i]>0:      
    pass
  else:
    j = i+d
    while j < h*w and j-d>=0:
      pos_j = dic[j]
      pos_jd = dic[j-d]
      A[j] = A[j-d] + abs(pos_j[1]-pos_jd[1]) + abs(pos_j[0]-pos_jd[0])    
      j += d        
  i+=1
  
for i in range(q):
  print(A[R[i]-1] - A[L[i]-1])  