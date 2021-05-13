n = int(input())
a = list(map(int, input().split()))

a.sort()

now = 0

ans = []

for i in range(n-2):
    if a[i+1] > 0:
        ans.append([a[0], a[i+1]])
        a[0] = a[0] - a[i+1]
    else:
        ans.append([a[n-1], a[i+1]])
        a[n-1] = a[n-1] - a[i+1]

ans.append([a[n-1],a[0]])
print(a[n-1]-a[0])

for i in ans:
    print(i[0],i[1])