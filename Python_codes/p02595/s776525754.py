n,d=map(int, input().split())
xy = [map(int, input().split()) for _ in range(n)]
yx= set(xy)
xy=list(yx)
x, y = [list(i) for i in zip(*xy)]
d2=d*d
count=0
for i in range(n):
    xi=x[i]
    yi=y[i]
    if xi*xi+yi*yi<=d2:
        count+=1

print(count)