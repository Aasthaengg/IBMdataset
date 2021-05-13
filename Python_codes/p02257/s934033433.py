def is_prime(x):
    if x == 2:
        return True
    
    if x < 2 or x % 2 == 0:
        return False

    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    
    return True


N = int(input())
cnt = 0
for _ in range(N):
    i = int(input())
    cnt += is_prime(i)
print(cnt)

