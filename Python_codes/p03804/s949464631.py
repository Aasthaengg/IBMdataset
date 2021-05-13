#!/usr/bin/env python3

def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))

def main():
    N, M = MII()
    A = []
    for _ in range(N):
        A.append(list(input()))

    B = []
    for _ in range(M):
        B.append(list(input()))

    f = True
    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(M):
                if A[i+k][j:j+M] != B[k]:
                    f = False
                    break
                f = True
            if f:
                print('Yes')
                return
    
    print('No')

if __name__ == '__main__':
    main()
