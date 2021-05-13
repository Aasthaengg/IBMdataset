n = int(input())
i = 1
cnt = 0
while i <= n:
    if len(str(i)) % 2 >= 1:
        cnt += 1
    i += 1
print(cnt)