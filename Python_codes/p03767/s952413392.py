N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse = True)

sum = 0
for i in range(1, N+1):
    sum += a[2 * i - 1]
print(sum)
