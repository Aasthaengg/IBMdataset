
n = int(input())
da = [list(map(int,input().split())) for i in range(n)]

now = da[0]
for i in range(1,n):
    co = max((now[0] - 1)// da[i][0], (now[1] - 1)// da[i][1])
    co += 1
    now[0] = da[i][0] * co
    now[1] = da[i][1] * co
print(now[0] + now[1])