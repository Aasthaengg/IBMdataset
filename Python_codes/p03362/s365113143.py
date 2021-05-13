import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def get_sieve_of_eratosthenes(n):
    """
    エラトステネスの篩
    """
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        return []
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit < p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
    return deque(data)

def main():
    N = int(input())

    """
    小さい素数から順に題意を満たすものを列挙するのはそもそも不可能らしい。
    結論は構成問題でした。５で割ってあまり１の素数を列挙すれば良いという、、、
    """

    ans = []
    cnt = 0
    for p in get_sieve_of_eratosthenes(55555):
        if cnt == N: break
        if p % 5 == 1:
            ans.append(p)
            cnt += 1
    print(" ".join(map(str, ans)))



if __name__ == "__main__":
    main()
