Q = int(input())

import math
def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)
    for serial in range(3, num, 2):
        if serial >= sqrt:
            return input_list
        for s in range(serial ** 2, num, serial): 
            input_list[s] = False

primes = sieve_of_erastosthenes(10**5)
likes = []
for i in range(3, 10**5, 2):
    if primes[i] and primes[(i+1)//2]:
        likes.append(i)

from bisect import bisect_left, bisect_right

for _ in range(Q):
    l, r = map(int, input().split())
    print(bisect_right(likes, r) - bisect_left(likes, l))