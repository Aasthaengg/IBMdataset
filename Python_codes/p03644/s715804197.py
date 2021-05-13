n = int(input())

ans = 0
t = 0
for i in range(1, n+1):
    a = i
    tmp = 0
    while i % 2 == 0:
        tmp += 1
        i //= 2
    if tmp >= t:
        t = tmp
        ans = a

print(ans)