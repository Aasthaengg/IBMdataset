n,d = map(int,input().split())
ans = 0
for i in range(n):
    p,q = map(int,input().split())
    r = (p**2 + q**2)**0.5
    if r <= d:
        ans += 1
print(ans)