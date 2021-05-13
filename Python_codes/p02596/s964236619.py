k = int(input())

n = 7 % k
ans = -1
cnt = 1
checked = {n}
while n > 0:
    n = (n * 10 + 7) % k
    cnt += 1
    if n in checked:
        break
    checked.add(n)

if n == 0:
    print(cnt)
else:
    print(-1)
