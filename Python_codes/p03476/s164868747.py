def prime(p):
    primeFlag = True
    if p == 1:
        primeFlag = False
    for i in range(2,(int(p**0.5)+1)):
        if p%i==0:
            primeFlag = False
            break
    if primeFlag:
        return True
    else:
        return False
    
Q = int(input())

memo = [0]*100001

for i in range(2,100001):
    first = prime(i)
    second = prime((i+1)//2)
    if first and second:
        memo[i] = 1

for i in range(1,100001):
    memo[i] = memo[i-1]+memo[i]

for i in range(Q):
    l,r = map(int,input().split())
    print(memo[r]-memo[l-1])