n,a,b = map(int, open(0).read().split())

ans = 0
for i in range(1,n+1):
    tmp = sum(map(int,list(str(i))))
    if a<=tmp<=b:
        ans += i
print(ans)