n = int(input())
cnt = 0
for i in range(1, n + 1):
    temp = 0
    while i > 0:
        i //= 10
        temp += 1
    if temp % 2 != 0:
        cnt += 1
print(cnt)
