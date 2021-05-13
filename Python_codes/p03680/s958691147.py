N = int(input())
A = [0] + [int(input()) for _ in range(N)]

done = {}
ans = 0
now = A[1]
while True:
    ans += 1
    if now == 2:
        print(ans)
        exit(0)
    if done.get(now) == None:
        done[now] = True
        now = A[now]
    else:
        break
print(-1)