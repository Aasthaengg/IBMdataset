import sys
import math
import itertools
import collections
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N = NI()
    XL = [NLI() for _ in range(N)]
    
    #print(XL)
    arm_range = []
    for n in range(N):
        arm_range.append([XL[n][0]-XL[n][1],XL[n][0]+XL[n][1]])
    #print(arm_range)
    
    sorted_arm_range = sorted(arm_range, key=lambda x: x[1])  #[1]に注目してソート
    #print(sorted_arm_range)
    
    ans = 1
    arm_end = sorted_arm_range[0][1]
    
    if N == 1:
        ans = 1
    else:
        for n in range(N-1):
            if sorted_arm_range[n+1][0] >= arm_end:
                arm_end = sorted_arm_range[n+1][1]
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()