n = int(input())
a = list(map(int, input().split()))

res = 0
for i in range(1, n):
    if a[i] == a[i - 1]:
        a[i] = 101
        res += 1

print(res)