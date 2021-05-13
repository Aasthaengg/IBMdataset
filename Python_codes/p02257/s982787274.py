from sys import stdin
import math
def isPrime(x):
    if x == 2 or x == 3: return True
    elif (x < 2 or x % 2 == 0 or x % 3 == 0): return False
    s = int(math.sqrt(x) + 1)
    for i in range(5, s + 1, 2):
        if x % i == 0: return False
    return True
n = int(stdin.readline())
cnt = 0
for i in range(0, n):
    if isPrime(int(stdin.readline())): cnt += 1
print(cnt)