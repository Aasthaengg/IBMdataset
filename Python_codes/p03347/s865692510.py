n = int(input())
ans = 0
now = int(input())
if now != 0:
    print(-1)
    exit()
zero = 0
for i in range(n-1):
    a = int(input())
    if a == now + 1:
        ans += 1
        now = a
    elif a <= now:
        ans += a
        zero = i-a
        now = a
    elif a >= now + 2:
        print(-1)
        exit()
print(ans)