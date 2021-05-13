# One Quadrillion and One Dalmatians
from string import ascii_lowercase as alp
N = int(input())

# 27進法に直す
def f(n):
    digits = []
    while n != 0:
        n -= 1
        rem = n % 26
        digits.append(rem)
        n = n // 26
    return digits

ans = ''.join([alp[e] for e in f(N)])[::-1]
print(ans)