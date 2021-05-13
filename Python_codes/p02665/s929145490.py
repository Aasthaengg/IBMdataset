#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = list(map(int, input().split()))
    leaf = sum(A)
    M = [0]*(N+1)
    if N==0:
        if A[0]==1:
            print(1)
            exit()
        else:
            print(-1)
            exit()
    if A[0]==1:
        print(-1)
        exit()
    M[0] = 1
    for i in range(1,N+1):
        M[i] = 2*M[i-1] - A[i]
        leaf -= A[i]
        M[i] = min(M[i],leaf)
        if M[i] < 0:
            print(-1)
            exit()
    print(sum(M)+sum(A))
    
if __name__ == '__main__':
    main()
