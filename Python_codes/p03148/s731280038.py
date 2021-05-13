# ABC 116 D - Various Sushi
N, K = map(int,input().split())

# S[k] := ネタkのおいしさのリスト
S = [[-float("inf")] for k in range(N)]
for k in range(N):
    t, d = map(int,input().split())
    S[t-1].append(d)

# 各種類のおいしさの最大を入れた配列がtop、それ以外がhoka
# それらを降順にソートして、k=1,2,..Kについて、topから大きい順にk個、hokaから同様にN-k個取ると、種類はk以上になる
# hokaからの要素で合計の種類がkより大きくなるばあい、その要素以上の大きさで同じ種類のものがtopに入っているため、
# あとでその種類からもtopを取る場合に、合計点がより大きい組み合わせになる
top = []
hoka = []
for k in range(N):
    S[k].sort()
    top.append(S[k].pop())
    hoka += S[k]

top.sort(reverse=True)
hoka.sort(reverse=True)

# 毎回sum(top[:k])とかやっていると間に合わないので累積和
# hokaから一つも取らないときは0を返すようにする
T = [0 for k in range(N+1)]
H = [0 for k in range(N+1)]
T[1], H[1] = top[0], hoka[0]
for k in range(2,N):
    T[k] = T[k-1] + top[k-1]
    H[k] = H[k-1] + hoka[k-1]

ans = 0
for k in range(1,K+1):
    ans = max(ans,T[k]+H[K-k]+k**2)
print(ans)