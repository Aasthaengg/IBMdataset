import math

n,k = map(int,input().split())
a = list(map(int,input().split()))

def cal(lis,x):
    an = 0
    for i in range(len(lis)):
        an += (math.ceil(lis[i] / x) - 1)
        
    return an

left = 0
right = 10**9

for i in range(100):
    m = (left + right) / 2
    
    b = cal(a,m)
    
    if b > k:
        left = m
    else:
        right = m
        
print(math.ceil(m))