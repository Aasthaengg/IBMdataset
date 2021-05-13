INF = 10 ** 9
MOD = 10 **9 + 7
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  collections import deque
from math import factorial

def main():
    n = int(input())
    B = list(map(int,input().split()))
    flag = True
    ans = []
    for i in range(n):
        idx = -1
        for j in range(n - i):
            if B[j] == j + 1:
                idx = j
        if idx == -1:
            flag = False
            break
        ans.append(idx + 1)
        B = B[:idx] + B[idx + 1:]

        if not flag:
            break
    
    print('\n'.join(map(str,ans[::-1])) if flag else -1)
if __name__=='__main__':
    main()
