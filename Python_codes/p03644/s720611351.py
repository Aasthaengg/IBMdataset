n = int(input())

ans = 1
cnt = 0

for i in range(2, n + 1):
    c = 0
    num = i
    while num % 2 == 0:
        c += 1
        num = num // 2
    if cnt < c:
        cnt = c
        ans = i
print(ans)
