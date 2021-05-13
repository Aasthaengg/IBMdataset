n,m=map(int,input().split())
comb = []
for _ in range(m):
    comb.append(list(map(int,input().split()))[1:])
point = list(map(int,input().split()))
ans = 0
for i in range(2**n): #スイッチのon/offの組み合わせは2**n通りある
    on = [0]*m
    for j in range(n): #それぞれ何個めがonになっているか調べる
        if (i>>j)&1: #j個目がonになっているとき
            for k in range(m): #それぞれの電球に対して
                if j+1 in comb[k]: #もしj個目のon/offが電球kに関係するなら
                    on[k] += 1 #電球kに関してonポイントを与える
                    on[k] %= 2 #onポイントは偶奇のみ議論する
    if point==on: #もしこの組み合わせのon/offパターンが所与の条件に一致するなら
        ans += 1 #全ての電灯が一致する組み合わせが一つ見つかったことになる
print(ans)