n = int(input())
ans = 0
while 0 < n:
    if n % 10 == 2: ans += 1
    n //= 10
print(ans)