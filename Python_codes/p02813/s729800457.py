import math
n = int(input())
pli = list(map(int,input().split()))
qli = list(map(int,input().split()))
a,b = 0,0
for i in range(n-1):
    a += (pli[i]-1)*(math.factorial(n-1-i))
    for j in range(n-1-i):
        if pli[j+i+1] > pli[i]:
            pli[j+i+1] -= 1
for i in range(n-1):
    b += (qli[i]-1)*(math.factorial(n-1-i))
    for j in range(n-1-i):
        if qli[j+i+1] > qli[i]:
            qli[j+i+1] -= 1
print(abs(a-b))