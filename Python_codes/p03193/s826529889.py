# CADDi 2018 for Beginners: B – AtCoder Alloy
N, H, W = [int(s) for s in input().split()]
R = [[int(s) for s in input().split()] for _ in range(N)]

count = 0

for i in range(N):
    if R[i][0] >= H and R[i][1] >= W:
        count += 1

print(count)