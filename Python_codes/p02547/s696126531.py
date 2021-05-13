n = int(input())
cnt = 0
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    if a[i][0] == a[i][1]:
        cnt += 1
    else:
        cnt = 0
    if cnt == 3:
        print('Yes')
        exit()
print('No')