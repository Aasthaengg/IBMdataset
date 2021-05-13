n = int(input())

def fib(n):
 if(n==0): return 1
 elif(n==1): return 1
 elif(n>1):
   a,b = 1,1
   for i in range(n-1):
     a,b = b,a+b
   return b

print(fib(n))
