import math
X = int(input())

def is_prime(x):
    a = int(math.sqrt(X)) + 1
    for i in range(2,a):
        if x % i == 0:
            return False
    return True

for j in range(X,X+100):
    if is_prime(j):
        ans = j    
        break
print(ans)