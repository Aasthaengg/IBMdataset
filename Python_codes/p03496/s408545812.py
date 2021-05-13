import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)

def main():
    n = int(input())
    a = list(map(int,input().split()))

    m = INF
    idx_m = -1
    M = -INF
    idx_M = -1
    for i in range(n):
        if M < a[i]:
            idx_M = i
            M = a[i]
        if m > a[i]:
            idx_m = i
            m = a[i]
    
    ans = []
    flag = False
    
    if m == 0 and M == 0:
        print(0)
        exit()
    elif m < 0 and M > 0:
        if abs(m) <= abs(M):
            flag = True
    elif m >= 0:
        flag = True
    
    
    if flag:
        for i in range(n):
            if a[i] < 0:
                a[i] += M
                ans.append((idx_M + 1, i + 1))
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i+1] += a[i]
                ans.append((i + 1, i + 2))
    else:
        for i in range(n):
            if a[i] > 0:
                a[i] += m
                ans.append((idx_m + 1, i + 1))
        for i in range(n-2,-1,-1):
            if a[i] > a[i + 1]:
                a[i] += a[i+1]
                ans.append((i + 2, i + 1))
    
    l = len(ans)
    print(l)
    for i in range(l):
        print(*ans[i])

if __name__=='__main__':
    main()