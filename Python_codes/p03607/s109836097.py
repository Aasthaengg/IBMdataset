n = int(input())
a = {}

cnt = 0
for i in range(n):
    ai = int(input()) - 1

    if ai in a:
        cnt -= 1
        del a[ai]
    else:
        cnt += 1
        a[ai] = 1

print(cnt)