import math
def fib(q):
   fibonacci = [0,1]
   for i in range(2,q):
       fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
   return fibonacci[q-1]
n,m = list(map(int, input("").split()))
a=[]
a.append(-1)
for i in range(m):   
    a.append(int(input()))
a.append(n+1)
out=1
c=10**9+7
for i in range(m+1):
    out*=int(fib(a[i+1]-a[i]))
    out%=c
print(out)