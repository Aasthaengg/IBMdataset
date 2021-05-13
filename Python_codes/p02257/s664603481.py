def isPrime(num):
    if num == 2: return 1
    if num < 2 or num&1 == 0: return 0
    if pow(2, num-1, num) == 1: return 1
    return 0

n = input()
s = 0
for i in xrange(n):
    s += isPrime(input())

print s