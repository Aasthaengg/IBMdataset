import math
import bisect
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
result=[]
a=int(input())
for i in range(a-500,a+501):
    if i<0:
        continue
    if is_prime(i):
        result.append(i)
bisect.insort_left(result,a)
n=bisect.bisect_left(result,a)
print(result[n+1])