n = int(input())
a = [int(input()) for _ in range(n)]

bn, cnt = 1, 0
for _ in range(n):
    if bn == 2:
        print(cnt)
        exit()
    else:
        bn = a[bn-1]
        cnt += 1

print('-1')

