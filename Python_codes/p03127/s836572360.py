import functools
import math
N = int(input())
A = list(map(int, input().split()))
print(functools.reduce(lambda x,y:math.gcd(x,y),A))