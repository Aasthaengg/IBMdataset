INF = 10 ** 9
MOD = 10 ** 9 + 7
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  math import factorial


def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if sum(a) < sum(b):
        print(-1)
        return
    c = [p - q for p,q in zip(a,b)]
    c.sort(reverse=True)
    minus = 0
    ans = 0
    for i in range(n - 1,-1,-1):
        if c[i] < 0:
            minus += c[i]
            ans += 1
        else:
            break
    
    for i in range(n):
        if minus >= 0:
            break
        minus += c[i]
        ans += 1
    print(ans)
if __name__ == '__main__':
    main() 