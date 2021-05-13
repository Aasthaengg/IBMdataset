a,b,c = map(int,input().split())
if any([i%2==0 for i in (a,b,c)]):
    print(0)
    exit()
else:
    ans = min(a*b , c*b , a*c)
print(ans)