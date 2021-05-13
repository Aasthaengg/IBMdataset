import sys
import numpy as np

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return is_prime


def main():
    prime = primes(10**5)
    like2017 = [False]*(10**5+1)
    for i in range(1,10**5+1,2):
        if prime[i] and prime[(i+1)//2]:
            like2017[i] = True
    like2017 = np.array(like2017).cumsum()

    Q = int(readline())
    for _ in range(Q):
        l,r = map(int, readline().split())
        print(like2017[r]-like2017[l-1])

if __name__ == '__main__':
    main()
