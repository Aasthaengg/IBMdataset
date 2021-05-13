n = int(input())
p = list(map(int, input().split()))
min = 10 ** 100
count = 0


for i in range(n):
    if p[i] < min:
        min = p[i]
        count += 1

print(count)
