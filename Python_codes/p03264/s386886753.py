k = int(input())
n = k//2
a = n*(n+1)//2
x = (k-1)%2
print(a*2 - x*n)