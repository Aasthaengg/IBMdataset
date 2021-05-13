#n,kが小さい
#xi,yi全て試す

#for ループ変更
import itertools
n,k = map(int, input().split( ))

p = []
x = []
y = []
for i in range(n):
    xi,yi = map(int, input().split( ))
    p.append((xi,yi))
    x.append(xi)
    y.append(yi)

y = list(set(y))
x = list(set(x))
x.sort()
y.sort()
lx = len(x)
ly = len(y)
ans = 10**20
for xi,xj in itertools.combinations(x,2):
    for yi,yj in itertools.combinations(y,2):
        cnt = 0
        for xk,yk in p:
            if xi <= xk and xk<=xj and yi <=yk and yk<=yj:
                        cnt += 1
        if cnt >= k:
            ans = min(ans, (xj-xi)*(yj-yi))
print(ans)
                    

