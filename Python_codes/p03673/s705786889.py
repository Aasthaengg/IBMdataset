from collections import *
n = int(input())
a = [int(i) for i in input().split()]

b = deque()

b.append(a[0])
for i in range(1, n):
    if(i%2 == 1):
        b.append(a[i])  
    else:
        b.appendleft(a[i])
   

if(n % 2 == 0):
    b.reverse()
    

print(' '.join(map(str, b)))
