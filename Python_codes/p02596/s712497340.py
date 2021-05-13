k = int(input())
a = [0 for _ in range(k)]
n = 7

a[0] = 7 % k
for i in range(1, k):
    a[i] = (a[i - 1] * 10 + 7) % k

for i in range(0, k):
    if a[i] == 0:
        print(i + 1)
        exit(0)
print(-1)