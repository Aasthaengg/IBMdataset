#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import numpy as np

def main():
    n = int(input())
    mob=np.array(list(map(int,input().split())),dtype=int)
    bra=np.array(list(map(int,input().split())),dtype=int)
    ans=0

    for i in range(n):
        tmp1=min(mob[i],bra[i])
        ans += tmp1
        tmp2=min(mob[i+1],bra[i]-tmp1)
        ans += tmp2
        mob[i+1]-=tmp2
    print(ans)


if __name__=="__main__":
    main()