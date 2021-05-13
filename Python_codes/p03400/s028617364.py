n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]

sum = n
for i in range(n):
    j = 1 + a[i]
    while j <= d:
        sum += 1
        j += a[i]

sum += x
print(sum)

