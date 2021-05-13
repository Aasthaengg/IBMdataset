# 2125
# 方針．f(n)を求めるのがlog(N)で終わりそうだから普通に素直に実装すればいいのでは？
# ただし最初だけは別に実装する必要がある
N = int(input())
X = list(input())

# i番目のビットを反転させて,
# やってることは似てるはずなのになんかうまく行かない
dic={}
bn00 = X.count('1')
x00 = int(''.join(X),2)
aa = x00 % (bn00+1)
if bn00-1==0:
    bb = 0
else:
    bb = x00 % (bn00-1)
for i in range(N):
    # ちゃんともとに戻してね，ということで本のビット
    b = int(X[i]) & 1
    bn = b ^ 1
    if bn:
        bn0 = bn00 + 1
        x0 = aa
    else:
        bn0 = bn00 - 1
        x0 = bb
    if bn0==0: # ビットが全く立っていないつまり0の時，0%0はエラーを起こすので，n%0もエラーを起こす
        print(0)
        continue
    if b: # もとのビットが立っている場合は減らす，ここの計算量が一番重いので計算量を削減してみる
        xi = x0 - b * pow(2,N-1-i,bn0)
    if bn:
        xi = x0 + bn * pow(2, N - 1 - i, bn0)
    xi %= bn0
    num = xi
    count = 1
    while num > 0:
        p = format(num,'b').count('1') # 10進数を２進数にかえるなら，これがいいのかも,int(str(i),2)を使うっていう手もあるけど周りくどい
        num = num % p
        count += 1
    print(count)
