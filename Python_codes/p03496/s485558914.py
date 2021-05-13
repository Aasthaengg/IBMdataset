import sys
import math
from fractions import gcd
# import queue
# from collections import Counter
# from itertools import accumulate
# from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def combination_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

big_prime = 1000000007

"""
# 標準入力取得
## 文字列
 =  sys.stdin.readline().rstrip()
 =  list(sys.stdin.readline().rstrip())

## 数値
 =  int(sys.stdin.readline())
 =  map(int, sys.stdin.readline().split())
 =  list(map(int, sys.stdin.readline().split()))
 =  [list(map(int,list(sys.stdin.readline().split()))) for i in range(N)]
"""

N = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))

a_max = max(list_a)
a_min = min(list_a)

ans = []

if (a_max == a_min):
    cnt = 0
elif (math.fabs(a_max) > math.fabs(a_min)):
    # for a in list_a:
    #     a += math.fabs(a_max)
    newList = [item + a_max for item in list_a]
    # print(newList)
    for i in range(N):
        # print(format(list_a.index(max(list_a))+1) + " " + format(i+1))
        ans.append((list_a.index(max(list_a))+1, i+1))

    newList2 = newList
    for i in range(N-1):
        # if (newList2[i] > newList2[i+1]):
            newList2[i+1] += newList2[i]
            ans.append((i+1, i+2))


else:
    # for a in list_a:
    #     a -= math.fabs(a_min)
    newList = [item + a_min for item in list_a]
    for i in range(N):
        # print(format(list_a.index(min(list_a))+1) + " " + format(i+1))
        ans.append((list_a.index(min(list_a))+1, i+1))

    newList2 = newList
    # for i in range(N-1):
    #     if (newList2[(N-1)-i] < newList2[(N-1)-(i+1)]):
    #         newList2[(N-1)-(i+1)] += newList2[(N-1)-i]
    #         # print(format((N-1)-i+1) + " " + format((N-1)-i))
    #         ans.append(((N-1)-i+1, (N-1)-i))
    for i in range(N-1, 0, -1):
        # if (newList2[i] < newList2[i-1]):
            newList2[i-1] += newList2[i]
            ans.append((i+1, i))

# print(list_a)
# print(newList)

print(len(ans))
for i in range(len(ans)):
    s, t = ans[i]
    print(s, t)
