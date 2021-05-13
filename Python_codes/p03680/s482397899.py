N = int(input())
a = [int(input()) for _ in range(N)]
a.insert(0, 0)
next = 1
ans = 0
for i in range(N):
    next = a[next]
    ans += 1
    if next == 2:
        print(ans)
        break
else:
    print(-1)
