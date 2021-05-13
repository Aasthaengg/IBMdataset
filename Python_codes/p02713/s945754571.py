#162
import math
from functools import reduce

def gcd(*number):
    return reduce(math.gcd, number)

K = int(input())
combinations = []
combinations.extend([[i+1]*3 for i in range(K)])
for i in range(K):
    combinations.extend([[i+1,i+1,j+1] for j in range(K) if j>i])
    for j in range(K):
        combinations.extend([[i+1,j+1,k+1] for k in range(K) if (j>i and k>j)])
result=0
for combination in combinations:
    a, b, c = combination
    if(a==b and b==c):
        result += a
    elif((a==b and b!=c) or (b==c and c!=a) or (c==a and a!=b)):
        result += gcd(a,b,c)*6
    else:
        result += gcd(a,b,c)*6
    
print(result)