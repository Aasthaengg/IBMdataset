#nの素因数分解を行い、リスト[[素因数,指数],....]を返す
# 2020 = 2^2 * 5^1 * 101^1
#[[2,2],[5,1],[101,1]
def prime_factorize(n):
    #返す配列
    res = []
    for i in range(2,n+1):
        #指数
        ex = 0
        # √Nまで行う
        if i * i > n:
            break
        if n % i != 0:
            continue
        #iで割り続ける
        while ( n % i == 0):
            ex += 1
            n /= i
        #その結果を追加
        res.append([i,ex])
    #最後に残った数について、1でなければ素数なのでリストに加える
    if n != 1:
        res.append([int(n),1])

    return res


N = int(input())
MOD = 1000000007
#exp[p] = 素因数pの指数
exp = [0] * (N+1)

for i in range(2,N+1):
    pf = prime_factorize(i)
    for j in range(len(pf)):
        exp[pf[j][0]] += pf[j][1]

ans = 1
for i in range(2,N+1):
    #約数の個数は(exp +1)の積
    ans *= exp[i] + 1
    ans %= MOD

print(ans)
