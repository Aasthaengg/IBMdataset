import itertools
N=int(input())

fmat=[]
for i in range(N):
  array=list(map(int,input().split()))
  fmat.append(array)
  
pmat=[]
for i in range(N):
  array=list(map(int,input().split()))
  pmat.append(array)
#print(fmat)
#print(pmat)

max_answer=-10**9
for bit in itertools.product(range(2),repeat=10):
  if sum(bit)==0:
    continue
    
  answer=0  
  for i in range(N):
    both_num=0
    for j in range(10):
      if bit[j]==1 and fmat[i][j]==1:
        both_num+=1
    
    answer+=pmat[i][both_num]
    
  max_answer=max(max_answer,answer)
  
print(max_answer)