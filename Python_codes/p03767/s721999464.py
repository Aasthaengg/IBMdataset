n = int(input())
a = list(map(int, input().split(" ")))

a.sort(reverse=True)
sum = 0
for i in range(1, 2 * n, 2):
    sum += a[i]

print(sum)