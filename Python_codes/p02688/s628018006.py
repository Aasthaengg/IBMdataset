n, k = list(map(int, input().split()))
snake = [0] * n
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in range(len(a)):
        snake[a[j] - 1] += 1
print(snake.count(0))