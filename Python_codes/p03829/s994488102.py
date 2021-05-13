n,a,b = map(int,input().split())
*l, = map(int,input().split())
ans = 0
for i in range(len(l)-1):
    ans += min(b,a*(l[i+1]-l[i]))
print(ans)


