import itertools

n=int(input())
p=tuple(map(int,input().split()))
q=tuple(map(int,input().split()))
num=list(itertools.permutations(range(1,n+1)))
cnt,c1,c2=0,0,0

for i in num:
  cnt+=1
  
  if i==p:
    c1=cnt
    
  if i==q:
    c2=cnt
    
print(abs(c1-c2))