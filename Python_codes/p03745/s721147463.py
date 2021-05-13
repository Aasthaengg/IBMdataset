n = int(input())
a = list(map(int, input().split()))
ans = 1
trend = '-'
pre = a[0]
for now in a:
    if (trend=='<' and pre>now) or (trend=='>' and pre<now):
        ans += 1
        trend = '-'
    else:
        if pre<now:
            trend = '<'
        elif pre>now:
            trend = '>'
    pre = now
print(ans)