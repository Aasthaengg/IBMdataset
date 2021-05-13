import math


def is_prime(x):
    if x == 1:
        return False

    for y in range(2, math.ceil(math.sqrt(x)) + 1):
        if not x % y:
            return False
    return True


def submit():
    n = int(input())

    # 55555以下の素数を求める
    prime_cand = []
    for x in range(2, 55556):
        if is_prime(x):
            prime_cand.append(x)

    # mod 5で1のものに絞る
    prime_cand = [p for p in prime_cand if p % 5 == 1]
    print(*prime_cand[:n])
        

submit()