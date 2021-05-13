N = int(input())
a = sorted(list(map(int, input().split())))

total = 0
for i, num in enumerate(a[N:]):
    if i % 2 == 0:
        total += num

print(total)