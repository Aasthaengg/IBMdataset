import sys
import numpy as np
from math import factorial

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, A, B = lr()
V = np.array(lr())
V.sort()
if A == 1:
    ave = V[-A]
else:
    ave = V[-A:].sum() / A
print(ave)
left_i = np.searchsorted(V, V[-A], side='left')
right_i = np.searchsorted(V, V[-A], side='right')
num = right_i - left_i
done = N - right_i

bottom = A-done
top = B-done

def combinations_count(n, r):
    ''' 組み合わせ '''
    return factorial(n) // (factorial(n - r) * factorial(r))

answer = combinations_count(num, bottom)
if ave == V[-A] and num > 1:
    for i in range(bottom+1, min(num, top)+1):
        answer += combinations_count(num, i)

print(answer)
# 15