n,m = map(int,input().split())
xyz = [0]*n
for i in range(n):
    xyz[i] = list(map(int,input().split()))
ans = 0
for i in range(2**3):
    lis = [1,1,1]
    for j in range(3):
        if (i>>j)&1:
            lis[j] = -1
    c = [0]*n
    for i,[x,y,z] in enumerate(xyz):
        c[i] += lis[0]*x + lis[1]*y + lis[2]*z
    c = sorted(c,reverse=True)
    d = sum(c[:m])
    ans = max(ans, d)
print(ans)