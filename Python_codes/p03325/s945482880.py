n,*aa = map(int, open(0).read().split())

ans = 0
for a in aa:
    while a%2==0:
        ans += 1
        a//=2

print(ans)