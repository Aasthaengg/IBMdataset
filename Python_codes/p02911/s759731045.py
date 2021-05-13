import sys
N, K, Q = map(int, input().split())
points = [0] * N
for _ in range(Q):
    a = int(sys.stdin.readline())
    points[a-1] += 1
for point in points:
    if point > (Q - K):
        print("Yes")
    else:
        print("No")