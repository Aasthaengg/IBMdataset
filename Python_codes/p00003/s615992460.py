import math
N = int(input())
for _ in [0]*N:
    x = sorted(map(int, input().split()))
    print("YES" if x[2] == math.sqrt(x[0]**2+x[1]**2) else "NO")