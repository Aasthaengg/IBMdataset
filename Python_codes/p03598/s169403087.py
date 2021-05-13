N = int(input())
K = int(input())
balls = list(map(int, input().split()))

total_move = 0
for ball in balls:
    if ball < K - ball:
        total_move += ball * 2
    else:
        total_move += (K - ball) * 2
print(total_move)