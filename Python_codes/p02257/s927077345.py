import math

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

t = int(input())
cnt = 0
for i in range(t):
    if isPrime(int(input())):
        cnt +=1
print(cnt)

