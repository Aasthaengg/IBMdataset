# 解法 RとLで別々に偶数回とても大きな回数移動させたときにどこに行くかを記録する．
S = input()
import math

count = 0
# まずRについて，調べていく
A = [0 for _ in S]
for i,s in enumerate(S):
    if s == 'L':
        A[i-1] += math.ceil(count/2)
        A[i] += math.floor(count/2)
        count = 0
        continue
    count += 1
count = 0
lenA = len(A)
for i,s in enumerate(S[::-1]):
    if s == 'R':
        A[lenA-i] += math.ceil(count/2)
        A[lenA-i-1] += math.floor(count/2)
        count = 0
        continue
    count += 1
print(' '.join([str(a) for a in A]))
