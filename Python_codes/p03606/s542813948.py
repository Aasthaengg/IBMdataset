import sys
input = sys.stdin.readline

N = int(input())

seat = []
for _ in range(N):
    l, r = map(int, input().split())
    for x in range(l, r+1):
        seat.append(x)
print(len(seat))
