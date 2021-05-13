import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
from collections import defaultdict
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, P = map(int, readline().split())
    A = list(map(int, readline().split()))
    odd = 0
    even = 0
    for a in A:
        if a&1:
            odd += 1
        else:
            even += 1

    fact = [1, 1]
    for i in range(2, odd + 1):
        fact.append(fact[-1] * i)

    def nCr(n,r):
        return fact[n]//(fact[r]*fact[n-r])

    if P==0:
        tmp = 0
        for i in range(0, odd+1, 2):
            tmp += nCr(odd,i)
        ans = 2**even*tmp
    else:
        tmp = 0
        for i in range(1, odd+1, 2):
            tmp += nCr(odd,i)
        ans = 2**even*tmp

    print(ans)


if __name__ == '__main__':
    main()
