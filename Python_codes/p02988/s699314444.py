n = int(input())
p = [int(s) for s in input().split()]

count = 0

for i in range(1, n - 1):
    if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
        count += 1
print(count)