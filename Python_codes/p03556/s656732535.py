from math import sqrt
n=int(input())
while True:
    if sqrt(n)%1==0:
        print(n)
        break
    n-=1