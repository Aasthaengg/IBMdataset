from sys import stdin
input = stdin.buffer.readline
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

MOD = 10 ** 9 + 7

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

rest = N
zero = 0
zero_left, zero_right = 0, 0
tmp = []
for a, b in AB:
    if a == b == 0:
        zero += 1
        rest -= 1
    elif a == 0:
        zero_left += 1
    elif b == 0:
        zero_right += 1
    else:
        gcd_ab = gcd(abs(a), abs(b))
        a, b = a // gcd_ab,  b // gcd_ab
        if a < 0: a, b = -a, -b
        tmp.append([a, b])
AB = tmp

cnt = defaultdict(int)
for a, b in AB:
    cnt[(a, b)] += 1

answer = 1
answer *= pow(2, zero_left + zero_right, MOD) - (pow(2, zero_left, MOD) - 1) * (pow(2, zero_right, MOD) - 1)
answer %= MOD
rest -= zero_right + zero_left
#print("answer:", answer)

check = defaultdict(int)
for a, b in AB:
    if b > 0 and check[(a, b)] == 0:
        check[(a, b)] = 1
        answer *= pow(2, cnt[(a, b)] + cnt[(b, -a)], MOD) - (pow(2, cnt[(a, b)], MOD) - 1) * (pow(2, cnt[(b, -a)], MOD) - 1) 
        answer %= MOD
        rest -= cnt[(a, b)] + cnt[(b, -a)]

answer *= pow(2, rest, MOD)
answer += zero - 1
answer %= MOD
print(answer)