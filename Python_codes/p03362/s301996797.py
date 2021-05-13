import sys
import math

N = int(sys.stdin.readline().rstrip())

def sieve_of_erastosthenes(num):
    input_list = [
        False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True
        for i in range(num)
    ]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)

    for serial in range(3, num, 2):
        if serial >= sqrt:
            return [i for i, b in enumerate(input_list) if b == True]
        for s in range(serial**2, num, serial):
            input_list[s] = False

primes = sieve_of_erastosthenes(55555)

ans = []

for p in primes:
    if p % 5 == 1:
        ans.append(p)
    if len(ans) == N:
        break

print(" ".join(map(str, ans)))