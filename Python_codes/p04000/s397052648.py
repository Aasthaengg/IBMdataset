h,w,n = map(int, input().split())

# 黒マス black[y座標] = [x1,x2,...]
black = dict()

# 周囲に黒マスがあるマス
search = set()

for i in range(n):
    a,b = map(int, input().split())
    a-=1
    b-=1
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if 1<=a+y<h-1 and 1<=b+x<w-1:
                search.add((a+y,b+x))  # タプル。set()内にリストは格納できない。
    try:
        black[a][b]=1
    except:
        black[a]=dict()
        black[a][b]=1


ans = [0]*10
# 探索すべき全マスに対して、周囲の黒マスの数を数える。
for a,b in search:
    p = 0
    for y in [-1,0,1]:
        for x in [-1,0,1]:
            try:
                if black[a+y][b+x]==1:
                    p+=1
            except:
                continue
    ans[p]+=1
ans[0]=(h-2)*(w-2)-sum(ans[1:])

for a in ans:
    print(a)