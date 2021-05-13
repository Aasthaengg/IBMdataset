N,P=map(int,input().split())
A=list(map(int,input().split()))
g=k=0
for i in A:
    if i%2:
        k+=1
    else:
        g+=1
a=0
from math import factorial
if P:
    for i in range(1,k+1,2):
        a+=factorial(k)//factorial(i)//factorial(k-i)
else:
    for i in range(0,k+1,2):
        a+=factorial(k)//factorial(i)//factorial(k-i)
print(a*pow(2,g))