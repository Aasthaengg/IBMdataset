from random import randrange

def eratosthenes(size):
    table = [True] * (size + 1)
    table[0] = table[1] = True
    for i in range(2, int(round(pow(size+1, 0.5)))):
        if not table[i]:
            continue
        for j in range(i + i, size+1, i):
            table[j] = False
    return table

def miller_rabin(n, k=20):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    d = n - 1
    while d & 1 == 0:
        d >>= 1
    for _ in range(k):
        a = randrange(1, n)
        y = pow(a, d, n)
        t = d
        while (t != n - 1) and (y != 1) and (y != n - 1):
            y = pow(y, 2, n)
            t <<= 1
        if (y != n - 1 ) and ((t & 1) == 0):
            return False
    return True

if __name__ == "__main__":
    N = int(input())
    print(sum(map(miller_rabin, [int(input()) for _ in range(N)])))