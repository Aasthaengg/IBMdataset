n, m = map(int, input().split())
grida = []
gridb = []
for i in range(n):
    grida.append(list(input()))
for i in range(m):
    gridb.append(list(input()))

ans = False
for i in range(n-m+1):
    for j in range(n-m+1):
        bad = False 
        for k in range(m):
            for l in range(m):
                if grida[k+i][l+j] != gridb[k][l]:
                    bad = True
        if not bad:
            ans = True

if ans:
    print("Yes")
else:
    print("No")

