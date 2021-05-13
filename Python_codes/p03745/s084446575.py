n = int(input())
a = list(map(int, input().split()))
 
ans = 1
u = False
d = False
for i in range(1, n):
    if u:
        if a[i] < a[i - 1]:
            u = False
            ans += 1
    elif d:
        if a[i] > a[i - 1]:
            d = False
            ans += 1
    else:
        if a[i] > a[i - 1]:
            u = True
        elif a[i] < a[i - 1]:
            d = True
print(ans)