from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007

def solve():
    A,B,K = map(int, input().split())
    turn = 0
    while K > 0:
        if turn == 0:
            if A%2 == 1:
                A -= 1
            B += A/2
            A /= 2
            turn ^= 1
        else :
            if B%2 == 1:
                B -=1
            A += B/2
            B /= 2
            turn ^= 1
        K -= 1

    A = (int)(A)
    B = (int)(B)
    print(A,B)
            


        

if __name__ == '__main__':
    solve()
