n = int(input())
a = list(map(int, input().split()))
b = [0] * n
for i in range(n):
    count = 0
    multi = 1
    if n - i == 0:
        count = sum(b)
    else:
        while (n - i) * multi <= n:
            count += b[(n - i) * multi - 1]
            multi += 1
    if count % 2 != a[n - i - 1]:
        b[n - i - 1] += 1
print(sum(b))
if sum(b) == 0:
    exit()
for i in range(n):
    if b[i] == 1:
        print(i + 1, end=' ')