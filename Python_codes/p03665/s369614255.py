import sys
def input(): return sys.stdin.readline().strip()
import math
def resolve():
    n,p=map(int, input().split())
    l=list(map(int,input().split()))
    gu=0
    ki=0
    cnt=0
    for i in l:
        if i%2==1:
            ki+=1
        else:
            gu+=1
    if p==0:
        for j in range(0,ki+1,2):
            x=math.factorial(ki)//(math.factorial(ki-j)*math.factorial(j))
            for k in range(gu+1):
                y=math.factorial(gu)//(math.factorial(gu-k)*math.factorial(k))
                cnt+=x*y
    else:
        for j in range(1,ki+1,2):
            x=math.factorial(ki)//(math.factorial(ki-j)*math.factorial(j))
            for k in range(gu+1):
                y=math.factorial(gu)//(math.factorial(gu-k)*math.factorial(k))
                cnt+=x*y
    print(cnt)


resolve()