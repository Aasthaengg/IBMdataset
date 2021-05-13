import math
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
s=[]
n=int(input())
for i in range(2,55555):
    if is_prime(i)==True:
        if i%5==1:
            s.append(i)
print(' '.join(map(str, s[:n])))