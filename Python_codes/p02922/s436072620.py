a,b = map(int,input().split())
ans = 1
tmp = a
if b==1:
    print(0)
else:
    while tmp<b:
        tmp += a-1
        ans += 1
    print(ans)
