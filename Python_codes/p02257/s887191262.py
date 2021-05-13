def isprime(n):
    from math import floor,sqrt
    if n <= 1:
        return False
    for i in range(2,floor(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())
ans = []
for i in range(n):
    po = int(input())
    if isprime(po):
        ans.append(po)  
print(len(ans))
