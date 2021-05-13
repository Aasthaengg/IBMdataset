MOD = 10 ** 9 + 7
INF = 10 ** 12
import sys
sys.setrecursionlimit(1000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
import numpy as np

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    
    cnt = [0] * 2002
    ret = [0] * n
    for i in range(n):
        for j in range(a[i] + 1):
            cnt[j] += 1

        tmp = 0
        for j in range(i):
            if a[j] > a[i]:
                tmp += 1
        ret[i] = tmp
    
    ans = 0
    for i in range(n):
        ans += ret[i] * k
        ans %= MOD
        ans += cnt[a[i] + 1] * k * (k - 1)//2
        ans %= MOD
    print(ans)

if __name__ =='__main__':
    main()  