import sys
#import string
#from collections import defaultdict, deque, Counter
#import bisect
#import heapq
#import math
#from itertools import accumulate
#from itertools import permutations as perm
#from itertools import combinations as comb
#from itertools import combinations_with_replacement as combr
#from fractions import gcd
#import numpy as np

stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)
MIN = -10 ** 9
MOD = 10 ** 9 + 7
INF = float("inf")
IINF = 10 ** 18
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

def solve():
    x = int(stdin.readline().rstrip())
    p = factorization(x)
    num = []
    if x == 1:
        print(0)
        exit()
    for i in p:
        for j in range(i[1]):
            if x%(i[0] ** (j+1)) == 0:
                num.append(i[0] ** (j+1))
                x = x/(i[0] ** (j+1))
            else:
                break
    print(len(num))
    exit()



if __name__ == '__main__':
    solve()
