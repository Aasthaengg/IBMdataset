N, M = map(int, input().split())

A = [list(map(int, input().split()))[1:] for _ in range(N)]

ans = 0

for i in range(1, M + 1):
    for K in A:
        if K.count(i) == 0:
            break
    else:
        ans += 1

print(ans)