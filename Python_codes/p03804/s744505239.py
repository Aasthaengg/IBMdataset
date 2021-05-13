n, m = map(int, input().split())

nlis = [list(input()) for _ in range(n)]
mlis = [list(input()) for _ in range(m)]

f = 0

for i in range(n):
    for j in range(n):
        if i+m-1 >=n or j+m-1 >=n:
            continue

        flag = 1
        for k in range(m):
            for l in range(m):
                if nlis[i+k][j+l] != mlis[k][l]:
                    flag = 0
        
        if flag:
            f = 1

if f:
    print('Yes')
else:
    print('No')