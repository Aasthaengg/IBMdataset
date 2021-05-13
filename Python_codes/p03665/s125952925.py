from math import factorial
def ncr(n,r):
    a=factorial(n)
    b=factorial(n-r)*factorial(r)
    return a//b
N,P=list(map(int,input().split()))
A=list(map(int,input().split()))
A=[i%2 for i in A]
zero=[i for i in A if i==0]
one=[i for i in A if i==1]
lzero=len(zero)
lone=len(one)
if lzero==0:
    if P%2==0:
        a = 0
        for i in range(2, lone+1, 2):
            a += ncr(lone, i)
        print(a+1)
    else:
        a = 0
        for i in range(1, lone+1, 2):
            a += ncr(lone, i)
        print(a)
    exit()
if lone==0:
    if P%2==0:
        print(2**lzero)
    else:print(0)
    exit()
if P%2==1:
    guu=2**lzero
    a=0
    for i in range(1,lone+1,2):
        a+=ncr(lone,i)
    print(guu*a)
else:
    guu=2**lzero
    a=0
    for i in range(0,lone+1,2):
        a+=ncr(lone,i)
    print(guu*a)
