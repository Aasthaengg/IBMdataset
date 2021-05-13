n = int(input())
a = [int(s) for s in input().split()]
count = 0
for i in range(n):
    if (i + 1) % 2 == 1:
        if a[i] % 2 == 1:
            count += 1
print(count)