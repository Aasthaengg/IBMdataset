import sys
import math

input = sys.stdin.readline
MOD = 1000000007

N = int(input())

print(math.factorial(N)%MOD)
