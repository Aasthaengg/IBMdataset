"""
E.
"""
from functools import reduce
from collections import deque


def prod(x, y):
    return x * y % MOD

    
N, K = map(int, input().split())
a_list = list(map(int, input().split()))
a_list.sort(reverse=True)
# abs_a_list = sorted(a_list, key=abs, reverse=True)
MOD = 10**9 + 7

if K%2 == 1:
    flg = True
    for a in a_list:
        if a >= 0:
            flg = False
            break
    if flg:
        print(reduce(prod, a_list[:K]))
        exit()

S = []
a_list = deque(a_list)
i = 0
while i < K:
    if len(a_list)>=2:
        if a_list[0]*a_list[1] >= a_list[-1]*a_list[-2]:
            S.append(a_list.popleft())
            i += 1
        elif a_list[0]*a_list[1] < a_list[-1]*a_list[-2] and i <= K-2:
            S.append(a_list.pop())
            S.append(a_list.pop())
            i += 2
        else:
            S.append(a_list.popleft())
            i += 1
    else:
        S.append(a_list.popleft())
        i += 1
        
ans = reduce(prod, S)
print(ans)