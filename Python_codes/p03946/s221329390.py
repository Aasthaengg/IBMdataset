import sys
INF = 10**10
MOD = 10**9 + 7
sys.setrecursionlimit(100000000)
from functools import lru_cache
from itertools import permutations

def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))

    cummin = [0] * n
    cummax = [0] * n
    cummin[0] = a[0]
    cummax[-1] = a[-1]
    for i in range(1,n):
        cummin[i] = min(a[i],cummin[i - 1])
        cummax[- i - 1] = max(a[- i - 1],cummax[-i])
    
    ben = 0   
    for i in range(1,n):
        ben = max(ben,cummax[i] - cummin[i - 1])
    
    cnt = 0
    flag = True
    for i in range(1,n):
        if ben == cummax[i] - cummin[i - 1]:
            if flag:
                cnt += 1
                flag = False
            
        else:
            flag = True
    
    print(cnt)

if __name__=='__main__':
    main() 