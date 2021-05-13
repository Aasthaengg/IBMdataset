n = int(input())

ans = 0

a = 1
while a**2 < n and a*(a+1) < n:
    if n % a == 0:
        ans += n//a - 1
    a += 1

print(ans)