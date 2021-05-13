h,w=map(int,input().split())
s=["?"*(w+2)]+["?"+input()+"?" for _ in [0]*h]+["?"*(w+2)]
memo=[[None for _ in range(w)] for _ in range(h)]
cnt=0
for i in range(1,h+1):
    for j in range(1,w+1):
        if memo[i-1][j-1]==None:
            memo[i-1][j-1]=True
            maru=(s[i][j]==".")
            batsu=1-maru
            q=[(i,j)]
            while(q):
                qq=[]
                for k,l in q:
                    if s[k-1][l]!="?":
                        if memo[k-2][l-1]==None:
                            if s[k-1][l]!=s[k][l]:
                                memo[k-2][l-1]=True
                                qq.append((k-1,l))
                                if s[k-1][l]==".":
                                    maru+=1
                                else:
                                    batsu+=1
                    if s[k+1][l]!="?":
                        if memo[k][l-1]==None:
                            if s[k+1][l]!=s[k][l]:
                                memo[k][l-1]=True
                                qq.append((k+1,l))
                                if s[k+1][l]==".":
                                    maru+=1
                                else:
                                    batsu+=1
                    if s[k][l-1]!="?":
                        if memo[k-1][l-2]==None:
                            if s[k][l-1]!=s[k][l]:
                                memo[k-1][l-2]=True
                                qq.append((k,l-1))
                                if s[k][l-1]==".":
                                    maru+=1
                                else:
                                    batsu+=1
                    if s[k][l+1]!="?":
                        if memo[k-1][l]==None:
                            if s[k][l+1]!=s[k][l]:
                                memo[k-1][l]=True
                                qq.append((k,l+1))
                                if s[k][l+1]==".":
                                    maru+=1
                                else:
                                    batsu+=1
                q=qq
            cnt+=maru*batsu
print(cnt)