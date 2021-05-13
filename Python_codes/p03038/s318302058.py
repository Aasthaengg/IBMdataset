from collections import Counter
[N,M] = list(map(int,input().split()))
A = list(map(int,input().split()))

D = dict(Counter(A))  #Aの要素の個数を数える。
for i in range(M):
    B,C = list(map(int,input().split()))
    D[C] = D.get(C,0) + B  #DのCがBあるっていう情報追加
# print(D)

K = sorted(list(D.keys()),reverse=True)  #Dのkeyを降順にソート
# print(K)

out = 0
cnt = 0 #N回で終了
now = 0
while cnt<=N-1:
    if D[K[now]] > 0: #大きい順に、D[K[now]]かい繰り返す
        out += K[now]
        D[K[now]] -= 1
        cnt+=1
    else:
        now+=1
print(out)