MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from bisect import bisect_left,bisect_right
from collections import deque

def main():
    n = int(input())
    food = []
    ans = 0
    for _ in range(n):
        a,b = map(int,input().split())
        ans -= b
        food.append(a + b)
    
    food.sort(reverse = True)
    for i in range(n):
        if i%2 == 0:
            ans += food[i]
    print(ans)
if __name__ =='__main__':
    main()  