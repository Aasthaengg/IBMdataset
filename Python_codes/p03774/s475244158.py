N,M = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]
c = [list(map(int,input().split())) for _ in range(M)]
for i in a:
    ans = 10**9
    num = 0
    for j in c:
        if abs(i[0]-j[0]) + abs(i[1]-j[1]) < ans:
            num = c.index(j)+1
        ans = min(ans, abs(i[0]-j[0]) + abs(i[1]-j[1]))
    print(num)