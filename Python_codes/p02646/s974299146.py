from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580


def solve():

    A,V = map(int, input().split())
    B,W = map(int, input().split())
    T = int(input().rstrip())
    if(B < A):
        V *= -1
        W *= -1
    if (A-B)*(A + T*V - B -T*W) <= 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
