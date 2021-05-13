import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


n = int(input())

ans = []

for i in range(11111):
    if is_prime(5*(i+1)+1):
        ans.append(5*(i+1)+1)
        if len(ans) == n:
            for j in range(n):
                print(ans[j], end=' ')
            print()
            exit()
