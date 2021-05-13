n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
point_sum = 0

for i in range(1, n+1):
    point_sum += a[i*2 - 1]

print(point_sum)