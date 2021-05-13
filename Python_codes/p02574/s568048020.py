import math
from functools import reduce

n = int(input())
a_list = list(map(int, input().split()))
max = 10 ** 6 + 1
memo = [0] * max

for a in a_list:
    memo[a] += 1

for i in range(2, max):
    if sum(memo[i::i]) > 1:
        if reduce(math.gcd, a_list) == 1:
            print("setwise coprime")
            exit()
        else:
            print("not coprime")
            exit()

print("pairwise coprime")
