h,w,a,b = map(int,input().split())
ans = [[0 for j in range(w)] for i in range(h)]
for i in range(h):
    for j in range(w):
        if i<b:
            if j>=a:
                ans[i][j] = 1
        else:
            if j<a:
                ans[i][j] = 1

for i in ans:
    print(''.join(map(str,i)))
