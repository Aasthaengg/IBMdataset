n = int(input())
a = [-1]
for i in range(n):
    a.append(int(input()))

ans = 0
cur = 0
for i, item in enumerate(a[::-1]):
    if i == 0:
        cur = item
        ans += item
        continue
    cur -= 1
    if cur < item:
        ans += item
        cur = item
    elif cur == item:
        continue
    elif cur > item:
        print(-1)
        exit()
print(ans)