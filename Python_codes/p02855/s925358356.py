h,w,k = map(int,input().split())
cake = []
ans = [[0]*w for _ in range(h)]
color = 1
for i in range(h):
    cake.append(list(input()))
for i in range(h):
    cur = 0
    for j in range(w):
        if cake[i][j] == "#":
            cur = color
            color += 1
            if j > 0 and ans[i][j-1] == "0":
                for k in range(j):
                    ans[i][k] = str(cur)
        ans[i][j] = str(cur)
flag = True
for i in range(h):
    for j in range(w):
        if ans[i][j] != "0":
            flag = False
        elif flag:
            k = i
            while ans[k][j] == "0":
                k += 1
            ans[i][j] = ans[k][j]
        else:
            k = i
            while ans[k][j] == "0":
                k -= 1
            ans[i][j] = ans[k][j]
for i in range(h):
    print(" ".join(ans[i]))            