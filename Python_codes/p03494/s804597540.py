n=int(input())  
A=list(map(int, input().split()))
a=[]
for i in range(n):
  for j in range(10**9):
    if A[i]%(2**(j+1))!=0:
      a.append(j)
      break 
print(min(a))
