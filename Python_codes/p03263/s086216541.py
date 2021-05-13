# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
H,W = map(int, input().split())
a = [list(map(int, input().split())) for i in range(H)]

#左上から右下に向かって探索
ans =[]
for h in range(H):
    for w in range(W-1):
        if a[h][w] %2 ==1:
            a[h][w] -=1
            a[h][w+1] +=1
            ans.append((h+1,w+1,h+1,w+2))
for i in range(H):
    if a[i][W-1] %2 ==1:
        if i !=H-1:        
            a[i][W-1] -=1
            a[i+1][W-1] +=1
            ans.append((i+1,W,i+2,W))


print(len(ans))
for i in range(len(ans)):
    print(*ans[i])