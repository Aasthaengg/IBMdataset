#!/usr/bin/env python3

def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))

def main():
    K, T = MII()
    A = LII()

    A.sort()
    cnt = A[-1] - sum(A[:-1]) - 1
    print(cnt if cnt > 0 else 0)

if __name__ == '__main__':
    main()
