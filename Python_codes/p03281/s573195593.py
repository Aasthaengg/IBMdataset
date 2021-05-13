import math
import collections
import fractions
import itertools
import functools
import operator

def yakusu_rekkyo(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def solve():
    n = int(input())
    cnt = 0
    for i in range(1,n+1):
        hoge = 0
        for j in yakusu_rekkyo(i):
            if j%2 == 1:
                hoge += 1
        if hoge == 8:
            cnt += 1
    print(cnt)
    return 0

if __name__ == "__main__":
    solve()