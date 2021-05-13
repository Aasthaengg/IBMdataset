import sys
# input = sys.stdin.readline
S = list(input())
p = 10 ** 9 + 7
# p = 10 ** 18

A = AB = ABC = 0
power = 1
for i, Si in enumerate(S):
    # print("#", A, AB, ABC)
    if Si == 'A':
        A = (A + 1 * power) % p
    elif Si == 'B':
        AB = (AB + A) % p
    elif Si == 'C':
        ABC = (ABC + AB) % p
    else:
        ABC = (3 * ABC + AB) % p
        AB = (3 * AB + A) % p
        A = (3 * A + 1 * power) % p
        power = (power * 3) % p

print(ABC)