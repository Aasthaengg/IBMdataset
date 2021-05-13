from collections import Counter

from scipy.misc import comb
#a = comb(n, r, exact=True)

N, A, B = list(map(int, input().split()))
V = list(map(int, input().split()))

V.sort(reverse = True)
C = Counter(V)

print(sum(V[:A]) / A)

max_value = V[0]

# V[0], ... V[A-1] がすべて同じとき、そうでないときで異なる
# V[0], ... V[A-1] に異なるものが含まれると、Aコ選ぶときがMAX
key_value = V[A-1]
if key_value < max_value:
  # V[A-1]の個数と、その前に何個あるかを数えればよい
  forward_item_count = 0
  for k,v in C.items():
    if k > key_value:
      forward_item_count += v

  print(int(comb(C[key_value], A - forward_item_count, exact=True)))
  exit(0)
  
# すべて同じときはAコ～Bコ選んでも平均一緒。組み合わせ数を足していく必要性
ans = 0
cnts = C[key_value]
for i in range(A,B+1):
  ans += comb(cnts,i, exact=True)
  
print(int(ans))