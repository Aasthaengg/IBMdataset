H,W = map(int,input().split())
a =[list(map(int,input().split())) for i in range(H)]


serching_pair = False
pair_count = 0
ans = []
#蛇行運転しながら奇数ペアを見つけるたびに出力
for i in range(H):
    if i%2 == 0:#左から右
        for j in range(0,W,1):
            if a[i][j]%2==1:
                if serching_pair:
                    ans[pair_count].append([i+1,j+1])
                    pair_count+=1
                    serching_pair=False
                else:
                    ans.append([[i+1,j+1]])
                    serching_pair=True
            else:
                if serching_pair:
                    ans[pair_count].append([i+1,j+1])

    else:#右から左
        for j in range(W-1,-1,-1):
            if a[i][j]%2==1:
                if serching_pair:
                    ans[pair_count].append([i+1,j+1])
                    pair_count+=1
                    serching_pair=False
                else:
                    ans.append([[i+1,j+1]])
                    serching_pair=True
            else:
                if serching_pair:
                    ans[pair_count].append([i+1,j+1])

ans_size=0
for i in range(0,pair_count,1):
    ans_size+=len(ans[i])-1
print(ans_size)

for i in range(0,pair_count,1):
    for j in range(1,len(ans[i])):
        print(" ".join(list(map(str,ans[i][j-1]+ans[i][j]))))


