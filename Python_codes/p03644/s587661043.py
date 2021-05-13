n = int(input())

if n == 1:
    ans = 1
else:
    i = 0
    now = 1
    while now < n:
        now *= 2
        i+=1
    if now > n:
        ans = now//2
    else:
        ans = now
print(ans)