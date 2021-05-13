N,M = [int(hoge) for hoge in input().split()]
A = [int(hoge) for hoge in input().split()]
S = sum(A)
kijun = (S-1)//(4*M)#これ以下ならダメ
X = (sum([a>kijun for a in A]))
if X < M:
    print("No")
else:
    print("Yes")