import itertools
import sys
input = sys.stdin.readline

def prime_boolean_table(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i + i, n + 1, i):
                primes[j] = False
    return primes

def main():
    pl = prime_boolean_table(10**5)
    ql = [0]*(10**5+1)
    for i in range(1,10**5+1):
        if pl[i] and pl[(i+1)//2]:
            ql[i] += 1
    ql = list(itertools.accumulate(ql))
    q = int(input())
    for _ in range(q):
        l,r = map(int,input().split())
        print(ql[r]-ql[l-1])

if __name__=='__main__':
    main()
