n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
b_next = 0
ans = 0
for i in range(n):
    if b_next >= a[i]:
        ans += a[i]
        b_next = b[i]
    elif b_next < a[i]:
        if b[i] < a[i] - b_next:
            ans += b_next + b[i]
            b_next = 0
        elif b[i] >= a[i] - b_next:
            ans += a[i]
            b_next = b[i] - (a[i] - b_next)
ans += min(a[n], b_next)
print(ans)