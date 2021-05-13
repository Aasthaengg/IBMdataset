h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]

ans = []
flag = False

for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            if a[i][j] % 2 == 1:
                flag = not flag
            if flag:
                if j != w - 1:
                    ans.append((i,j,i,j+1))
                else:
                    if i != h - 1:
                        ans.append((i,j,i+1,j))
    else:
        for j in range(w-1,-1,-1):
            if a[i][j] % 2 == 1:
                flag = not flag
            if flag:
                if j != 0:
                    ans.append((i,j,i,j-1))
                else:
                    if i != h - 1:
                        ans.append((i,j,i+1,j))

print(len(ans))
for i in ans:
    print(i[0]+1,i[1]+1,i[2]+1,i[3]+1)
