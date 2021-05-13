N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for lr in LR:
  cnt += lr[1] + 1 - lr[0]
print(cnt)