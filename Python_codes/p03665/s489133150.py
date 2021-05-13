import itertools
import math
from math import factorial

N,P = list(map(int, input().split()))
As = list(map(int, input().split()))

#奇数の袋、偶数の袋の個数を求める。
odd = 0
even = 0

for A in As:
    if(A % 2 == 0):
        even += 1
    else:
        odd += 1

#偶数の組み合わせを求める。
#偶数の組み合わせは0~N個のすべての組み合わせである。
even_combi = 0

for i in range(even+1):
    even_combi += math.factorial(even) // math.factorial(i) // math.factorial(even-i)

#print(even_combi)

#奇数の組み合わせを求める。
#奇数の組み合わせは、Pの値によって変わる。

#Pが0の時
odd_combi = 0

if(P == 0):
    for i in range(0,odd + 1,2):
        odd_combi += math.factorial(odd) // math.factorial(i) // math.factorial(odd-i)

else:
    for i in range(1, odd + 1 , 2):
        odd_combi += math.factorial(odd) // math.factorial(i) // math.factorial(odd-(i))

print(odd_combi*even_combi)