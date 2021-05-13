n, k = map(int, input().split())

maximum = (n-1) * (n-2) // 2
if k > maximum:
    print(-1)
    exit()

print(n - 1 + maximum - k)

for i in range(2, n+1):
    print(1, i)

remainder = maximum - k
for i in range(2, n):
    for j in range(i+1, n+1):
        if remainder <= 0:
            exit()
        print(i, j)
        remainder -= 1