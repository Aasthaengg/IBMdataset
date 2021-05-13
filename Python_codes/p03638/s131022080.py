h,w = map(int,input().split())
n = int(input())
lst1 = list(map(int,input().split()))
ans = [[0]*w for _ in range(h)]
ret = lst1[0]
color = 1
for i in range(h):
    if i%2 == 0:
        for j in range(w):
            if ret:
                ans[i][j] = color
                ret -= 1
            else:
                ret = lst1[color]
                color += 1
                ans[i][j] = color
                ret -= 1

    else:
        for j in range(w-1,-1,-1):
            if ret:
                ans[i][j] = color
                ret -= 1
            else:
                ret = lst1[color]
                color += 1
                ans[i][j] = color
                ret -= 1

for i in ans:
    print(" ".join(map(str,i)))