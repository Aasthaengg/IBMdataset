n = int(input())
la = [int(input())-1 for _ in range(n)]

pushed = set()

now = 0
ans = 0
while True:
    if now in pushed:
        ans = -1
        break
    pushed.add(now)
    ans += 1
    now = la[now]
    if now == 1:
        break
print(ans)
