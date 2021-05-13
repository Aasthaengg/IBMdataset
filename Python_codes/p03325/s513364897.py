n=int(input())
A=list(map(int,input().split()))
cnt=0

def f(x):
  tmp=0
  while x%2==0:
    tmp+=1
    x=x/2
  return tmp

for i in range(n):
  cnt+=f(A[i])
 
print(cnt)