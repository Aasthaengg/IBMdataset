import math
n=int(input())
a=list(map(int,input().split()))
num=a[0]
def g(num1,num2):
    return math.gcd(num1,num2)
for i in range(n-1):
    num=g(num,a[i+1])
print(num)
