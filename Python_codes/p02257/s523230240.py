def is_prime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
                
        return True
        
n = int(input())
count = 0

for _ in range(n):
    m = int(input())
    if is_prime(m):
        count += 1

print(count)