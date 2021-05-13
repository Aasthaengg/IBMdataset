import sys
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def factorial(n):
    if n == 1: return 1
    ret = 1
    for i in range(2, n + 1):
        ret *= i
        ret %= mod
    return ret

def main():
    N, M = map(int, input().split())
    if abs(N - M) > 1:
        print(0)
        return
    if N != M:
        print((factorial(M) * factorial(N)) % mod)
    else:
        print((factorial(M) * factorial(N) * 2) % mod)

if __name__ == "__main__":
    main()
