import sys
from itertools import accumulate
input=sys.stdin.buffer.readline
def main():
    n,k=map(int,input().split())
    a=[*map(int,input().split())]
    for _ in range(min(k,41)):
        b=[0]*n
        for i,t in enumerate(a):
            if i>t:b[i-t]+=1
            else:b[0]+=1
            j=i-~t
            if j<n:b[j]-=1
        a=[*accumulate(b)]
    print(' '.join(map(str,a)))
main()