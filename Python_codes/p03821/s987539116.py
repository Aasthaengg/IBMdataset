n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in range(n-1, -1, -1):
    if (a[i][0]+cnt)%a[i][1] != 0:
        cnt += a[i][1] - ((a[i][0]+cnt)%a[i][1])
print(cnt)