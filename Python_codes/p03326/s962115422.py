N,M = map(int,input().split())
xyz = []
for i in range(N):
    ii = list(map(int,input().split()))
    xyz.append(ii)

xyz2 = [sorted(xyz,key = lambda x:((-1)**a)*x[0]+((-1)**b)*x[1]+((-1)**c)*x[2]) for a in range(2) for b in range(2) for c in range(2)]
ans = 0
for xyz1 in xyz2:
    x1 = 0
    y1 = 0
    z1 = 0
    for x,y,z in xyz1[:M]:
        x1 += x
        y1 += y
        z1 += z
    ans = max(ans,abs(x1)+abs(y1)+abs(z1))
print(ans)