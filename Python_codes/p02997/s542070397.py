# coding: utf-8
# Your code here!
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    n, k = map(int, input().split())
    val = (n-1)*(n-2)//2
    if k > val:
        print(-1)
    else:
        rem = val-k
        print(n-1+rem)
        for i in range(2,n+1):
            print(1,i)
        a, b = 2, 3
        cnt = 0
        for i in range(rem):
            print(a,b)
            if b < n:
                b+=1
            else:
                a += 1
                b = a+1



resolve()
