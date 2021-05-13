from functools import lru_cache

N = int(input())
X = input()


@lru_cache(maxsize=None)
def popcount(x):
    return x % bin(x).count('1')


def f(x):
    cnt = 1
    while x > 0:
        x = popcount(x)
        cnt += 1

    return cnt


count = X.count('1')
mod_one = count - 1
if mod_one == 0:
    mod_one = 1
mod_zero = count + 1
ones = [1 % mod_one]
zeros = [1 % mod_zero]
x_mod_one = 0 if X[-1] == '0' else 1 % mod_one
x_mod_zero = 0 if X[-1] == '0' else 1 % mod_zero

for xi in reversed(X[:-1]):
    ones.append(ones[-1] * 2 % mod_one)
    zeros.append(zeros[-1] * 2 % mod_zero)
    if xi == '1':
        x_mod_one += ones[-1]
        x_mod_one %= mod_one
        x_mod_zero += zeros[-1]
        x_mod_zero %= mod_zero

ones = list(reversed(ones))
zeros = list(reversed(zeros))

for i in range(N):
    if count == 1 and X[i] == '1':
        print(0)
    elif X[i] == '1':
        x = (x_mod_one - ones[i]) % mod_one
        print(f(x))
    else:
        x = (x_mod_zero + zeros[i]) % mod_zero
        print(f(x))
