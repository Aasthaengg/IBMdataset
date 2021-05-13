n = int(input())

a = list(map(int, input().split()))
a.append(0)
a.insert(0,0)
a_abs = []
for i in range(n+1):
    a_abs.append(abs(a[i]-a[i+1]))

a_abs_max = sum(a_abs)
for i in range(1,n+1):
    ans = a_abs_max - abs(a[i]-a[i+1]) - abs(a[i]-a[i-1]) + abs(a[i+1]-a[i-1])
    print(ans)