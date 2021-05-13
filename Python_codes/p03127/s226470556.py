# 最大公約数(mathは3.5以降) 
import math
from functools import reduce
def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

# 初期入力
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

ans =gcd_list(A)
print(ans)
