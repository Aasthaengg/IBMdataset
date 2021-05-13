import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

bridge = [
    tuple(map(int,
              sys.stdin.readline().rstrip().split())) for _ in range(M)
]
bridge = sorted(bridge, key=lambda x: x[1])

ans = 0
t = 0
for a, b in bridge:
    if a >= t:
        ans += 1
        t = b
print(ans)