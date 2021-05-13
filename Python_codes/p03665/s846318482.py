#3問目
import itertools
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N, P = map(int, input().split())
A = list(map(int, input().split()))
#偶数グループと奇数グループにわける
odd = []
even = []
c = 0
for i in A:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
#奇数グループは組み合わせの総数を出す
#もしP=1なら奇数グループから奇数個を出す組み合わせの数、P=0なら奇数グループから偶数個を出す組み合わせの数
if P == 1:
    #奇数グループから奇数個を出す組み合わせの数
    for i in range(1, len(odd)+1, 2):
        c += combinations_count(len(odd), i)
if P == 0:
    #奇数グループから偶数個を出す組み合わせの数
    for i in range(0, len(odd)+1, 2):
        c += combinations_count(len(odd), i)
        
print(2 ** len(even) * c) 