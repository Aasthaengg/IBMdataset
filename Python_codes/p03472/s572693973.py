n,h = map(int,input().split())
A = []
B = []
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

#aの最大値を求める。
maxa = max(A)

#maxaのうち、bが最小の刀を求める。これを刀ｓとする。刀ｓを取り除く
minb = 10**10
s = 0
for i in range(n):
    if A[i] == maxa and B[i] < minb:
        minb = B[i]
        s = i
B.pop(s)

#bを降順に並べ、maxaより大きいbは投げつける
B.sort(reverse = True)
for i in range(len(B)):
    if B[i] > maxa:
        h = h - B[i]
        ans += 1
        if h <= 0:
            print(ans)
            exit()
    else:
        break

#まずsを投げてからaで割る
h = h - minb
ans += 1
if h <= 0:
    print(ans)
else:
    ans += (h+(maxa-1)) // maxa
    print(ans)