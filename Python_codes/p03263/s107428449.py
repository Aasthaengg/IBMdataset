h,w=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(h)]

cnt=0
ans=[]
for i in range(h):
    for j in range(w):
        if a[i][j]%2==1:
            if i==h-1 and j==w-1:
                break
            cnt+=1
            if j!=w-1:
                ans.append([i+1,j+1,i+1,j+2])
                a[i][j]-=1
                a[i][j+1]+=1
            else:
                ans.append([i+1,j+1,i+2,j+1])
                a[i][j]-=1
                a[i+1][j]+=1

print(cnt)
for ans_i in ans:
    print(*ans_i)

