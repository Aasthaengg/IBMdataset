n = int(input())
ans = 0
cnt = 1
while n >= 1:
    ans += cnt
    n //= 2
    cnt *= 2
print(ans)