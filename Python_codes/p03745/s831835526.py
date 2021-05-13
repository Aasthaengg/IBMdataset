n = int(input())
a =list(map(int,input().split()))

ans = 1
now = a[0]
before = '-'
for i in range(1,n):
    if before == '-':
        if now > a[i]:
            before = 'D'
        elif now< a[i]:
            before = 'U'

    else:
        if before == 'U' and now > a[i]:
            ans += 1
            before = '-'
        elif before == 'D' and now < a[i]:
            ans += 1
            before = '-'
    now = a[i]

print(ans)
