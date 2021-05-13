n = int(input())

d, x = map(int, input().split())

count = x

for _ in range(n):
    a = int(input())
    for i, z in enumerate(range(1, d+1, a)):
        count += 1

print(count)