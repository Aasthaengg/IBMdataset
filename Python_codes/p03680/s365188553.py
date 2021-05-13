import sys
from collections import deque, Counter
def I(): return int(sys.stdin.readline().rstrip())

if __name__=='__main__':
    n = I()
    l = []
    for _ in range(n):
        l.append(I())
    c = [0]*n
    now = 0
    c[now] = 1
    for i in range(1,n+1):
        now = l[now]-1
        c[now] += 1
        if now==1:
            print(i)
            exit()
        if c[now]==2:
            print(-1)
            exit()
    exit()