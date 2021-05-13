import sys
input = sys.stdin.readline
INF = 10**10
MOD = 10**9 + 7
sys.setrecursionlimit(100000000)
from functools import lru_cache
from copy import deepcopy 

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = deepcopy(a)

    ans1 = 0
    if a[0] <= 0:
        ans1 += 1 - a[0]
        a[0] = 1
    
    for i in range(1,n):
        a[i] += a[i - 1]
        if a[i - 1] < 0 and a[i] <= 0:
            ans1 += 1 - a[i]
            a[i] = 1
        elif a[i - 1] > 0 and a[i] >= 0:
            ans1 += a[i] + 1
            a[i] = -1
    
    ans2 = 0
    if b[0] >= 0:
        ans2 += b[0] + 1
        b[0] = -1

    for i in range(1,n):
        b[i] += b[i - 1]
        if b[i - 1] < 0 and b[i] <= 0:
            ans2 += 1 - b[i]
            b[i] = 1
        elif b[i - 1] > 0 and b[i] >= 0:
            ans2 += b[i] + 1
            b[i] = -1
    
    ans = min(ans1,ans2)
    print(ans)

if __name__=='__main__':
    main() 