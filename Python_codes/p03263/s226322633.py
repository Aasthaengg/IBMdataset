H,W = map(int,input().split())
a = [list(map(int,input().split())) for i in range(H)]

ans = []
flag = False
before = []
for i in range(H):
    if i%2==0:
        for j in range(W):
            if (not flag) and a[i][j]%2==1:
                flag = True
                before = [i,j]
            elif flag and a[i][j]%2==1:
                flag = False
                ans.append([before[0]+1,before[1]+1,i+1,j+1])
            elif (not flag) and a[i][j]%2==0:
                pass
            else:
                ans.append([before[0]+1,before[1]+1,i+1,j+1])
                before = [i,j]
    else:
        for j in reversed(range(W)):
            if (not flag) and a[i][j]%2==1:
                flag = True
                before = [i,j]
            elif flag and a[i][j]%2==1:
                flag = False
                ans.append([before[0]+1,before[1]+1,i+1,j+1])
            elif (not flag) and a[i][j]%2==0:
                pass
            else:
                ans.append([before[0]+1,before[1]+1,i+1,j+1])
                before = [i,j]
N = len(ans)
print(N)
for i in range(N):
    print(*ans[i])