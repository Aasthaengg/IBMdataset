from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007

def solve():
    S = (input().rstrip())
    K = int(input().rstrip())
    for x in range(len(S)):
        if(x%K == 0):
            print(S[x],end="")


    print("")
if __name__ == '__main__':
    solve()
