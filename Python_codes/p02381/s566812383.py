from math import *
while True:
    n = int(input())
    if(n == 0 ): break
    data = list(map(int,input().split()))  
    a = sum(data) / n
    b = 0
    c = 0
    for i in data:
        b += pow(i-a,2)
    c = sqrt(b/n)
    
    print(c)
