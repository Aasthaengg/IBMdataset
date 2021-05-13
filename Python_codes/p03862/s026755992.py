n, x = map(int, input().split())
li_a = list(map(int, input().split()))
s = []
for i in range(n-1):
    s.append(li_a[i]+li_a[i+1])
ans = 0
for i in range(n-1):
    if s[i] >= x:
        k = s[i] - x
        if li_a[i+1] >= k:
            ans += s[i] - x
            if i != n-2:
                s[i+1] -= k
                li_a[i+1] -= k
        else:
            ans += s[i] - x
            if i != n-2:
                s[i+1] -= li_a[i+1]
                li_a[i] -= k-li_a[i+1]
print(ans)