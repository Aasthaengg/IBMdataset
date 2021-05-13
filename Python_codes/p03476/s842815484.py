import sys
input = sys.stdin.readline
import math

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

like_2017 = [is_prime(n) and is_prime((n+1)//2) for n in range(1, 100001, 2)]
cumsum = [0] * len(like_2017)
cumsum[0] = like_2017[0]
for i in range(1, len(cumsum)):
    cumsum[i] = cumsum[i-1] + like_2017[i]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l, r = l // 2, r // 2
    if l == 0:
        print(cumsum[r])
    else:
        print(cumsum[r] - cumsum[l-1])
