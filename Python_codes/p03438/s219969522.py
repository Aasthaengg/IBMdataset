n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0

for i in range(n):
    if a[i] > b[i]:
        k = a[i] - b[i]
        b[i] += k
        cnt += k

for i in range(n):
    if a[i] < b[i]:
        k = (b[i] - a[i]) // 2
        a[i] += 2 * k
        cnt -= k
        if a[i] < b[i]:
            a[i] += 2
            b[i] += 1

print('Yes') if cnt <= 0 else print('No')

