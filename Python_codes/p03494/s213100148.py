N = int(input())
A = list(map(int,input().split()))
def X(x):
  y = 0
  while x%2==0:
    x = x/2
    y = y+1
  return y
a = [X(A[i]) for i in range(0,N)] 
  
print(min(a))
