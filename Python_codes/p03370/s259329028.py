n, x, *m = map(int, open(0).read().split())
ans = 0
for i in sorted(m):
    if x>=i:
        x -= i
        ans+=1
print(ans+x//min(m))