H, W = map(int, input().split())
a = []
for _ in range(H):
    a.append(list(map(int, input().split())))
#print(a)

cnt = 0
ope=[]
for y in range(H):
    if y != H -1:
        for x in range(W):
            if a[y][x] % 2 == 1:
                a[y][x] -= 1
                a[y + 1][x] += 1
                cnt += 1
                ope.append([y+1,x+1,y+1+1,x+1])
    else:
        for x in range(W-1):
            if a[y][x] % 2 == 1:
                a[y][x] -= 1
                a[y][x+1] += 1
                cnt += 1
                ope.append([y+1,x+1,y+1,x+1+1])
print(cnt)
for el in ope:
    print(' '.join(list(map(str, el))))



