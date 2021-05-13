from random import random
import math
import re
import fractions

MOD = 10**9+7

N = input()
T = map(int, raw_input().split(" "))
A = map(int, raw_input().split(" "))
# N = 10**5
# A = T = [999999999] * 10**5

result = 1

for i in xrange(N):
    et = bt = ea = ba = 0
    if i == 0 or T[i] != T[i-1]:
        et = T[i]
    else:
        bt = T[i]
    if i == N-1 or A[i] != A[i+1]:
        ea = A[i]
    else:
        ba = A[i]
    if ea + et > 0:
        if ea * et > 0 and et != ea:
            result = 0
            break
        if (ea > bt and bt != 0) or (et > ba and ba != 0):
            result = 0
            break
    else:
        result *= min(ba, bt)
        result %= MOD
print(result % MOD)
