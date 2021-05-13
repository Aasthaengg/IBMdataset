n = int(input())
shop = [] # 10
profit = [] # 11
for i in range(n):
    shop.append(list(map(int,input().split())))
for i in range(n):
    profit.append(list(map(int,input().split())))
cond = [bin(i)[2:].zfill(10) for i in range(1,2**10)]
ans = -int(1e15)
for i in range(len(cond)):
    pro_cnt = 0
    tar = cond[i]
    for j in range(n):
        tar_shop = shop[j]
        cnt = 0
        for k in range(10):
            if int(tar[k]) & tar_shop[k] == 1:
                cnt += 1
        pro_cnt += profit[j][cnt]
    ans = max(ans, pro_cnt)
print(ans)







