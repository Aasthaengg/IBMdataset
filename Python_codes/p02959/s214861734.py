n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = sum(a)
for i in range(n):
    if b[i] > a[i]:
        b[i] -= a[i]
        a[i] = 0
        if b[i] > a[i + 1]:
            a[i + 1] = 0
        else:
            a[i + 1] -= b[i]
    else:
        a[i] -= b[i]
ans -= sum(a)
print(ans)
