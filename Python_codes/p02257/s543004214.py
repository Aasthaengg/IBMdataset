def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
c = 0
for _ in range(n):
    s = int(input())
    if prime(s):
        c+=1

print(c)