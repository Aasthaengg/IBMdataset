N, K = map(int, input().split())
sticks = sorted([int(s) for s in input().split()], reverse=True)
snake = [l for i, l in enumerate(sticks) if i < K]
print(sum(snake))