n = int(input())
a = [0] + [int(i) for i in input().split()] + [0]

sum = sum([abs(a[i+1]-a[i]) for i in range(n+1)])
for i in range(1, n+1):
    print(sum - abs(a[i]-a[i-1]) - abs(a[i+1]-a[i]) + abs(a[i+1]-a[i-1]))
