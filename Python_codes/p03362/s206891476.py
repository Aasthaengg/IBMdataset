N=int(input())
import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
ans=[]
for i in range(1,55555+1):
    if i%5==1:
        if is_prime(i):
            ans.append(i)
            if len(ans)==N:
                break
print(*ans)