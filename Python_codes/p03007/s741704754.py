n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = []
for i in range(1, n-1):
    if a[i] <= 0:
        ans.append([a[n-1], a[i]])
        a[n-1] += abs(a[i])

    else:
        ans.append([a[0], a[i]])
        a[0] -= a[i]
        
ans.append([a[n-1], a[0]])

print(a[n-1] - a[0])
for i in range(n-1):
    print(*ans[i])
