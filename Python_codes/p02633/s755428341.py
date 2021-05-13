from collections import defaultdict
from math import sin, cos, radians
it = lambda: list(map(int, input().strip().split()))
INF = float('inf')

def solve():
    X = int(input())
    ans = 0
    
    degree = 90
    
    x = y = 0
    while True:
        ans += 1
        x += cos(radians(degree))
        y += sin(radians(degree))
        degree = (degree + X) % 360
        if abs(x) < 1e-7 and abs(y) < 1e-7:
            return ans

if __name__ == '__main__':
    print(solve())