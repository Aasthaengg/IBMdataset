n, k = map(int, input().split())
lst = list(map(int, input().split()))

snake = 0
lst.sort(reverse=True)

for num in range(0, k):
    snake += lst[num]

print(snake)