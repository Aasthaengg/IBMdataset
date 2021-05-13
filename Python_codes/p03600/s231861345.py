n = int(input())
ary = [list(map(int,input().split())) for _ in range(n)]
ans = sum([sum(i) for i in ary])
for i in range(n):
    for j in range(n):
        flag = 0
        for k in range(n):
            if j == k or i == k:continue
            if ary[i][j] > ary[i][k] + ary[k][j]:print(-1);exit()
            if ary[i][j] == ary[i][k] + ary[k][j]:
                flag = 1
        if flag:ans -= ary[i][j]
print(ans//2)