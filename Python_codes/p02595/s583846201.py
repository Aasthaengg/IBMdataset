import math

n,d = map(int,input().split())

count = 0
for i in range(n) :
    p,q = map(int,input().split())
    if math.sqrt(p**2+q**2)<=d :
        count += 1

print(count)