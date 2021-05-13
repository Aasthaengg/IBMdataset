N, M = map(int, input().split())
D = [list(map(int,input().split())) for i in range(N)]

D.sort()
ans = 0

while M > 0:
    for i in D:
        if i[1] >= M:
            ans += M*i[0]
            M = 0
        else:
            ans += i[1]*i[0]
            M -= i[1]

print(ans)