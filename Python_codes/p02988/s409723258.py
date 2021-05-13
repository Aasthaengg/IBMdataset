N = int(input())
p = list(map(int, input().split()))

count = 0
for x in range(N - 2):
    if (p[x] < p[x + 1] and p[x + 1] < p[x + 2]) or (p[x] > p[x + 1] and p[x + 1] > p[x + 2]):
        count += 1
print(count)
