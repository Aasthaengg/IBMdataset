s=list(input())
n=len(s)
score=0
g_cnt,p_cnt=1,0
if s[0]=="p":
    score-=1
for i in range(1,n):
    if g_cnt==p_cnt:
        if s[i]=="p":
            g_cnt+=1
            score-=1
        elif s[i]=="g":
            g_cnt+=1
    elif p_cnt<g_cnt:
        if s[i]=="p":
            p_cnt+=1
        elif s[i]=="g":
            p_cnt+=1
            score+=1
print(score)
