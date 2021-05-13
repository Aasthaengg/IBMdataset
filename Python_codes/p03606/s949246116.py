n = int(input())
apple = []
for _ in range(n):
    apple.append(list(map(int, input().split())))
count = 0
for i in apple:
    count += i[1] - i[0] + 1
print(count)