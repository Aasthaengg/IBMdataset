import numpy as np
 
n, m = map(int, input().split())
 
cards = list(map(int, input().split()))
cards = np.array(cards, np.int64)
cards.sort()

bc = [list(map(int, input().split())) for _ in range(m)]
bc = np.array(bc, np.int64)

B = bc[:,0]
C = bc[:,1]
 
#並び替えた配列のidxをnparrayで取得
idx = C.argsort()
B = B[idx][::-1]
C = C[idx][::-1]
 
p = 0
for b,c in zip(B,C):
    cards[p:p+b] = np.maximum(cards[p:p+b], c)
    p += b

print(sum(cards))