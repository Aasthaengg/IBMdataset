# ABC127 D
from bisect import bisect_left as bl

f=lambda:map(int,input().split())
N,M=f()
A=list(f())
A.sort()
BC=[]
for _ in [0]*M:
    BC.append(tuple(f()))
BC.sort(key=lambda x:x[1])
res=0
num=0
def compare():
    # True => Aが大きい
    if not A:
        return False
    if not BC:
        return True
    return A[-1]>BC[-1][1]

while 1:
    if compare():
        res+=A.pop()
        num+=1
    else:
        b,c=BC.pop()
        if b+num<=N:
            res+=c*b
            num+=b
        else:
            res+=c*(N-num)
            num+=(N-num)
    if num==N:
        break
print(res)