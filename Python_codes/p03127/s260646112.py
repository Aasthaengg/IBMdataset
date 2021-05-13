import math
import functools
input()
print(functools.reduce(math.gcd,map(int,input().split())))