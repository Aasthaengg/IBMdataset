a = list(map(int, input().split()))
a.sort()

if a[0]%2 == a[1]%2 == a[2]%2 == 1:
    ans = a[0]*a[1]
else:
    ans = 0
print(ans)
