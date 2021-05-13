def isprime(n):
    check = 1
    if n == 2:
        pass
    elif n == 1 or n % 2 == 0:
        check = 0
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                check = 0
                break
            else:
                i += 2
    return check
        

n = int(input())
ans = 0
for k in range(n):
    a = int(input())
    ans += isprime(a)
    
print(ans)
