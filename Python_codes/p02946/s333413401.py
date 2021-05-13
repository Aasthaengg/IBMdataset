k, x = map(int, input().split())

min = x - k + 1
max = x + k - 1

num = []
for i in range(min, max + 1):
    num.append(i)

print(*num)
