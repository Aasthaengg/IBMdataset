n = int(input())
cnt = 0
for i in range(1, n + 1):
    str_num = str(i)
    if len(str_num) % 2 != 0:
        cnt += 1

print(cnt)

