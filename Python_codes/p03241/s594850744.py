import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N, M = map(int, input().split())

#  nの約数をO(root(n))で全列挙、
# sortするなら O(root(n) * root(n)log(root(n))) --> O(n * log(n))
def make_divisors(n):
    import math
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0: #割り切れるとき
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    divisors.sort(reverse = True)
    return divisors

lst = make_divisors(M)
for i in lst:
    if M // i >= N:
        print (i)
        break

