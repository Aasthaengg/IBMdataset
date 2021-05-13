n = int(input())
a = list(map(int, input().split()))

if 0 in a:
    print(0)
    exit(0)

acc = 1
for i in range(n):
    acc *= a[i]
    if acc > 10 ** 18:
        print(-1)
        exit(0)

print(acc)