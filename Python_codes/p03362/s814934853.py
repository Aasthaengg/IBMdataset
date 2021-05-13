#!/usr/bin/python3
# -*- coding:utf-8 -*-

from collections import defaultdict
import numpy

def sieve_of_eratosthenes(n):
  primes = [2]
  cands = numpy.array(list(range(3, n+1, 2)), dtype=numpy.int)
  while len(cands) != 0:
    prime = primes[-1]
    cands = cands[cands % prime != 0]
    if len(cands) == 0:
      break
    primes.append(cands[0])
  return primes

def main():
  n = int(input())
  k = 5
  primes = sieve_of_eratosthenes(55555) 
  counts = defaultdict(list)
  for prime in primes:
    counts[prime % k].append(prime)
    if len(counts[prime % k]) >= n:
      print(' '.join(list(map(str, counts[prime % k]))))
      return
    
    
if __name__=='__main__':
  main()

