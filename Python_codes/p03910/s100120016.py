n = int(input())

cnt = 0
for i in range(1, n + 1):
    cnt += i
    if n <= cnt:
        cnt -= n
        num = i
        break

for i in range(1, num + 1):
    if i == cnt:
        continue
    print(i)