def is_prime(num):
    if   num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3,int(num**0.5)+1,2):
            if num % i == 0:
                return False
        return True

n = int(input())
ans = 0

for _ in range(n):
    num = int(input())
    if is_prime(num):
        ans += 1
print(ans)
