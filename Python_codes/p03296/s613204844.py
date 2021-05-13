n = int(input())
a = list(map(int,input().split()))
x = a[0]
y = 1
ans = 0
for i in range(1,n):
    if a[i] == x:
        y += 1
    else:
        ans += y // 2
        x = a[i]
        y = 1
print(ans + y // 2)