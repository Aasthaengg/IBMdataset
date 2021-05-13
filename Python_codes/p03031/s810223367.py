n, m = map(int,input().split())
s = list(list(map(int, input().split())) for _ in range(m)) 
p = list(map(int,input().split()))
ans = 0
for i in range(1<<n):
    # 全switch(n)のon/offパターン数
    sw = [False]*m
    # 各電球の点灯リストを作成
    for j in range(m):
        # 各電球について
        cnt = 0
        for k in range(1,len(s[j])):
            if i>>s[j][k]-1&1:
                cnt += 1
        if cnt%2==p[j]:
            sw[j]=True
    if all(sw):
        ans+=1
print(ans)