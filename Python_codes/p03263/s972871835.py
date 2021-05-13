h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
n = 0
ans = []
for i in range(h):
    for j in range(w):
        if a[i][j]%2==0:continue
        if j<w-1:
            a[i][j] -= 1
            a[i][j+1] += 1
            n += 1
            ans.append([i+1,j+1,i+1,j+2])
        elif i<h-1:
            a[i][j] -= 1
            a[i+1][j] += 1
            n += 1
            ans.append([i+1,j+1,i+2,j+1])
print(n)
for i in ans:
    print(*i)
