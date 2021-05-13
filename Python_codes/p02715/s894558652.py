import sys
import os

def file_input():
    f = open('Beginner_Contest_162/input.txt', 'r')
    sys.stdin = f

def main():
    #file_input()

    N,K=map(int, input().split())   #K以下、Nの長さ

    tmp=[0]*(K+1)
    mod=10**9+7
    out=0

    for i in range(K,0,-1):
        tmp[i]=pow(K//i,N,mod)  #iの倍数はK/i個ある。それがN個並んでいる
        for j in range(i*2,K+1,i):
            tmp[i]-=tmp[j]
        out+=tmp[i]*i

    print(out%mod)

if __name__ == '__main__':
    main()
