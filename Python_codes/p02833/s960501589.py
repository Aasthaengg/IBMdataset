n = int(input())
if n % 2 == 1:
    print(0)
    exit()
ans = 0
n //= 2
while n > 0:
    ans += n // 5
    n //= 5
print(ans)