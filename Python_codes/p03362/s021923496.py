import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
def isPrime(n):
    if n == 1: return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return True

def main():
    n = II()
    pp = []
    p = 1
    cnt = 0
    while cnt < n:
        p += 10
        if isPrime(p): pp.append(p); cnt += 1
    print(*pp)

if __name__ == '__main__':
    main()
