import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    L = 1000

    N = NI()
    if N == 0:
        print(0)
        exit(0)

    s = 1 if N > 0 else -1
    n = abs(N)

    bit = [0] * L

    i = 0
    while n > 0:
        if n % 2:
            bit[i] += 1
            if s > 0 and i % 2 == 1 or s < 0 and i % 2 == 0:
                bit[i+1] += 1
        n //= 2
        i += 1

    for i in range(L-2):
        b = bit[i]
        if b > 1:
            b1 = bit[i+1]
            if b1 > 0:
                if b1 >= b//2:
                    bit[i+1] -= b//2
                    bit[i] = b % 2
                else:
                    bit[i+1] = 0
                    bit[i] -= b1 * 2
            if bit[i] > 1:
                bit[i+2] += bit[i] // 2
                bit[i+1] += bit[i] // 2
                bit[i] = bit[i] % 2

    bit.reverse()
    i = bit.index(1)
    print(*bit[i:],sep='')

if __name__ == '__main__':
    main()