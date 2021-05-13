n,C = map(int,input().split())

d = [0 for i in range(C)]
for i in range(C):
    d_xy =  list(map(int,input().split()))
    d[i] = d_xy

c = [0 for i in range(n)]
for i in range(n):
    c_xy =  list(map(int,input().split()))
    c[i] = c_xy

li0 = [0 for i in range(C)]
li1 = [0 for i in range(C)]
li2 = [0 for i in range(C)]

for i in range(n):
    for j in range(n):
        a=i+1
        b=j+1
        if (a+b)%3==0:
            li0[c[i][j]-1] += 1
        elif (a+b)%3==1:
            li1[c[i][j]-1] += 1
        elif (a+b)%3==2:
            li2[c[i][j]-1] += 1

ans = (10**3)*500*500


for c0 in range(C):
    for c1 in range(C):
        for c2 in range(C):
            cst = 0
            if (c0==c1) or (c1==c2) or (c2==c0):
                continue

            for i in range(C):
                cst += d[i][c0]*li0[i]
                cst += d[i][c1]*li1[i]
                cst += d[i][c2]*li2[i]
            ans = min(ans,cst)

print(ans)


