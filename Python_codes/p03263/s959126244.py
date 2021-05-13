h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int, input().split())))

ans = []
flg = 0
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            if a[i][j] % 2 == 1:
                flg += 1
            val = [i+1,j+1,i+1,j+2]
            if val[2] <= h and val[3] <= w and flg % 2 == 1:
                ans.append(val)
            elif val[2] < h and val[3] > w and flg % 2 == 1:
                ans.append([i+1,j+1,i+2,j+1])
    else:
        j = w-1
        while j >= 0:
            if a[i][j] % 2 == 1:
                flg += 1
            val = [i+1,j+1,i+1,j]
            if val[2] <= h and val[3] > 0 and flg % 2 == 1:
                ans.append(val)
            elif val[2] < h and val[3] <= 0 and flg % 2 == 1:
                ans.append([i+1,j+1,i+2,j+1])

            j -= 1
print(len(ans))
for i in range(len(ans)):
    print(' '.join(map(str,ans[i])))
