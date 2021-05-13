n, m = map(int, input().split())
a = sorted(list(map(int,input().split())))
ans = 0
for i in a:
    if m - i < 0:
        print(ans)
        exit()
    m -= i
    ans += 1
if m > 0:
    print(ans-1)
else:
    print(ans)