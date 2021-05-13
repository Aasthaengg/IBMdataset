s=input()
n=len(s)
ans=0
g_cnt=0
p_cnt=0
for i in range(n):
    # 判定
    if g_cnt>p_cnt:
        # パーを出す
        p_cnt+=1
        if s[i]=='g':
            ans+=1
    else:
        g_cnt+=1
        if s[i]=='p':
            ans-=1
print(ans)

