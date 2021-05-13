from functools import lru_cache

N,P = map(int, input().split())
A_list = [int(e) for e in input().split()]

A_odd_list = list()
A_even_list = list()

for A in A_list:
    if A%2 == 0:
        A_even_list.append(A)
    else:
        A_odd_list.append(A)

#######################################################################
#https://note.nkmk.me/python-math-factorial-permutations-combinations/
from operator import mul
from functools import reduce

@lru_cache(maxsize=100000000)
def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom
#######################################################################

choice_odd = 0
choice_even = 0
odds = len(A_odd_list)
evens = len(A_even_list)

if P == 1:
    #奇数の中から奇数個選ぶ
    for i in range(1,odds+1,2):
        choice_odd += combinations_count(odds,i)
    #偶数の中から好きな個数を選ぶ
    for i in range(0,evens+1,1):
        choice_even += combinations_count(evens,i)
else:
    #奇数の中から偶数個選ぶ
    for i in range(0,odds+1,2):
        choice_odd += combinations_count(odds,i)
    #偶数の中から好きな個数を選ぶ
    for i in range(0,evens+1,1):
        choice_even += combinations_count(evens,i)
        
print(choice_odd*choice_even)