n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

min = a[0]
max = a[n-1]

ans = []

for i in range(1,n-1):
    temp = a[i]
    if(temp < 0):
        ans.append('{} {}'.format(max, temp))
        max -= temp
    else:
        ans.append('{} {}'.format(min, temp))
        min -= temp

ans.append('{} {}'.format(max, min))
max -= min

print(max)

for i in range(n-1):
    print(ans[i])
