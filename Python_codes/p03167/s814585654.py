h,w = map(int,input().split())
mod = 10**9+7
a = [list(input()) for i in range(h)]
a[0][0] = 1
for i in range(1,w):
    if a[0][i] == '.':
        a[0][i] = a[0][i-1]
    else:
        a[0][i] = 0
for i in range(1,h):
    if a[i][0] == '.':
        a[i][0] = a[i-1][0]
    else:
        a[i][0] = 0
for i in range(1,h):
    for j in range(1,w):
        if a[i][j] == '.':
            a[i][j] = (a[i-1][j]+a[i][j-1])%mod
        else:
            a[i][j] = 0
print(a[-1][-1])