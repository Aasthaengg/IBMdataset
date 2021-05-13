import math
n = int(input())

def is_prime(x):
    sqrt_x = int(math.sqrt(x))
    for i in range(2, sqrt_x + 1):
        if x % i == 0:
            return False
    return True

iter = 0
ans = []
for i in range(2, 55556):
    if is_prime(i) and i % 5 == 1:
        ans.append(i)
        iter += 1
        
    if iter == n:
        break

print(" ".join(map(str, ans)))