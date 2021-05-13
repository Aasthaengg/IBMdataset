N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

flag = False
cnt = 0

for i in range(len(D)):
    if D[i][0] == D[i][1]:
        cnt += 1
        if cnt == 3:
            flag = True
    else:
        cnt = 0

print('Yes' if flag else 'No')