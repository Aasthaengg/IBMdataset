X = int(input())

cur = 100

ans = 0
while True:
    cur = int(cur * 101) // 100
    ans += 1
    if cur >= X:
        break
print(ans)
