# 解説見たつもりだけどまだWA
# https://atcoder.jp/contests/abc173/submissions/15052457
import sys
input = sys.stdin.readline

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
p = 10 ** 9 + 7
A.sort(key = lambda x : abs(x)) # 絶対値小→大
A_zpos = [a for a in A if a >= 0]
A_neg = [a for a in A if a < 0]

# 非負にできるか判定
nneg_en = False
if A_zpos:
    if K == N:
        if len(A_neg) % 2 == 0:
            nneg_en = True
    else:
        nneg_en = True
else:
    if K % 2 == 0:
        nneg_en = True


if nneg_en: # 非負にできる
    if K % 2 == 1:
        ans = A_zpos.pop() # 一番大きい正の数を確保
        K -= 1
    else:
        ans = 1

    while K > 0:
        # 2個ずつ取る
        next_zpos = -1 if len(A_zpos) < 2 else A_zpos[-1] * A_zpos[-2]
        next_neg = -1 if len(A_neg) < 2 else A_neg[-1] * A_neg[-2]
        if next_zpos >= next_neg:
            ans = ans * A_zpos.pop() * A_zpos.pop() % p
        else:
            ans = ans * A_neg.pop() * A_neg.pop() % p
        K -= 2
else:
    ans = 1
    for i in range(K):
        ans = ans * A[i] % p

print(ans)