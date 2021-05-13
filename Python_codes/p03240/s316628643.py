n = int(input())
x = [0] * n
y = [0] * n
h = [0] * n
for i in range(n):
    x2, y2, h2 = map(int, input().split())
    x[i] = x2
    y[i] = y2
    h[i] = h2
ans = [0,0,0]
for i in range(101):
    for j in range(101):
        l = 0
        while h[l] == 0:
            l += 1
        #print(l)
        val = h[l] + abs(i-x[l]) + abs(j-y[l])
        flg = True
        for k in range(n):
            if val != h[k] + abs(i-x[k]) + abs(j-y[k]) and h[k] != 0:
                flg = False
            if h[k] == 0 and abs(i-x[k]) + abs(j-y[k]) < val:
                flg = False
        if flg == True:
            ans = [i,j,val]
print(' '.join(map(str,ans)))
