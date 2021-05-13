from itertools import  product

n=int(input())

f=[list(map(int,input().split())) for _ in range(n)]
#曜日
p=[list(map(int,input().split())) for _ in range(n)]
#利益
ans=-10**50
for z in product((0, 1), repeat=10):#bit全探索のくみあわせを勝手に作ってくれるので使うとよい
    profit_count=0  #利益の合計
    for i in range(n):
        work_count=0  #働く時間帯が同じ回数
        for j in range(10):  #個数を調べる
            if f[i][j]==1 and z[j]==1:  #f[i][j]==z[j]だと両方0の時もcountしちゃう
                work_count+=1
        profit_count+=p[i][work_count]
    if ans<profit_count:  #ans=max(ans,profit_count)だと000000000000の時確認できない
        if 1 in z:   #１日以上働いているかの確認
            ans=profit_count
print(ans)