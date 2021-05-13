n = int(input())
a = [int(x) for x in input().split()]

a.append(0)
a.insert(0,0)

ans = 0

for i in range(1,n+2):
    ans += abs(a[i-1]-a[i])

for i in range(1,n+1):
    print(ans + abs(a[i-1] - a[i+1]) - (abs(a[i] - a[i-1]) + abs(a[i] - a[i+1])))
