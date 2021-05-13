
N = int(input())
Shop_info =[list(map(int, input().split())) for _ in range(N)]
Earn = [list(map(int, input().split())) for _ in range(N)]
ans = - float('inf')
for i in range(1,2**10):
    Open = [0] * N
    ansi = 0
    for j in range(10):
        if (i >> j) & 1 == 1:
            for k in range(N):
                if Shop_info[k][j]:
                    Open[k] += 1
    for x, o in enumerate(Open):
        ansi += Earn[x][o]
    ans = max(ans, ansi)
print(ans)