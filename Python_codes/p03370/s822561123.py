n, x = map(int, input().split())
apple = []
for _ in range(n):
    apple.append(int(input()))
count = len(apple)
x -= sum(apple)
count += x // min(apple)
print(count)