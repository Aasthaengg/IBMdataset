h,w,k=map(int,input().split())
s=[]
ans=[]
for i in range(h):
    s.append(list(input()))
    ans.append(['1']*w)
cnt=0
flag=0
flag2=0
for i in range(h):
    if flag2==0:
        cnt+=1
    if s[i].count('#')>0:
        flag = s[i].count('#')+cnt-1
        for j in range(w):
            ans[i][j]=str(cnt)
            if flag2>0:
                for k in range(1, flag2+1):
                    ans[i-k][j]=str(cnt)
            if s[i][j]=='#':
                if cnt != flag:
                    cnt+=1
        flag2=0
    else:
        flag2+=1
        if i == h-1:
            for j in range(w):
                for k in range(flag2):
                    ans[i-k][j]=ans[i-flag2][j]
        
for i in range(h):
    print(' '.join(ans[i]))