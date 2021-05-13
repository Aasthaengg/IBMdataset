n,m,x = map(int,input().split())
a = [0]*n
c = []
for i in range(n):
    a[i] = list(map(int,input().split()))
# 0 から (2^n)-1 までループ
for bit in range(1 << n):
    s = [0]*(m+1)

    for i in range(n):
        # bit に i 番目のフラグが立っているかどうか
        if bit & (1 << i):
            for j in range(m+1):
            # フラグが立っているならば sum に加算する
                s[j] += a[i][j]

    if all(s[j] >= x for j in range(1,m+1)):
        c.append(s[0])

if not c:
    print(-1)
else:
    print(min(c))