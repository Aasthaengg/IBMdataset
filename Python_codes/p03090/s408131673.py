from math import factorial

n=int(input())

print(factorial(n)//factorial(n-2)//2-n//2)

m = (n//2)*2
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if i+j != m+1:
            print(i,end=' ')
            print(j)