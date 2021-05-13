#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
from itertools import combinations

def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    counter=0
    mod = 10**9+7
    
    for i  in range(n-1):
        for j in range(i+1,n):
            if A[i] > A[j]: counter+=1

    y =0
    for a1 in A:
        for a2 in A:
            if a1 > a2: y+=1

    ans=(counter*k+y*k*(k-1)//2)%mod
    print(ans)

if __name__=="__main__":
    main()