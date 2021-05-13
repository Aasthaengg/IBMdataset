import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

def primes(array,n):
    C = collections.Counter(array)
    count = 0
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    for i in array:
      if is_prime[i]:
        if C[i] == 1: count += 1
        for j in range(i, n + 1, i):
            is_prime[j] = False
    return count

n = int(input())
A = list(map(int,input().split()))
A.sort()
data = [0] * (10**6+1)


print(primes(A,10**6))