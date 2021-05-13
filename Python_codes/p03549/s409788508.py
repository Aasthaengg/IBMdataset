n,m = map(int, input().split())
good=n-m
ok = 1/(2**m)
now_ok=ok
ans=0
x=1
nokori=1
while x<1000:
    tmp=(good*100+m*1900)*x
    now_ok = nokori * ok
    nokori -= now_ok
    tmp *= now_ok
    ans+=tmp
    x+=1

print(round(ans))