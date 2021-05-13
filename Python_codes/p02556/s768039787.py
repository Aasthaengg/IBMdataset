import sys
input = sys.stdin.readline

N = int(input())
points = [0] * N
rx = []
ry = []
for i in range(N):
    x, y = map(int, input().split())
    rx.append(x - y)
    ry.append(x + y)
print(max(max(rx) - min(rx), max(ry) - min(ry)))