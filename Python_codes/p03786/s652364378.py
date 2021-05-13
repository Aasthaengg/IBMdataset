n = int(input())
a = sorted(list(map(int, input().split())))

ans = -1
for i in range(n-1):
    if a[i]*2 < a[i+1]:
        ans = i
    a[i+1] += a[i]
print(n-ans-1)