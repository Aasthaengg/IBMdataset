N = int(input())
a = [int(input()) - 1 for _ in range(N)]

used = [False] * N

cur = 0
ans = 0
while not used[cur]:
    if cur == 1:
        print(ans)
        exit()

    used[cur] = True
    cur = a[cur]
    ans += 1

print(-1)