n,m = map(int,input().split())
lr = [list(map(int,input().split())) for i in range(m)]

max = 0
min = n+1
for i in range(m):
    if lr[i][0] > max :
        max = lr[i][0]
    if lr[i][1] < min :
        min = lr[i][1]

if min-max >= 0:
    print(min-max+1)
else :
    print(0)
