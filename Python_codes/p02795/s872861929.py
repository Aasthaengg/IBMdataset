H = int(input())
W = int(input())
N = int(input())

painted = 0
cnt = 0


for _ in range(min(H, W)):
    painted += max(H, W)
    cnt += 1
    if painted >= N:
        break

print(cnt)