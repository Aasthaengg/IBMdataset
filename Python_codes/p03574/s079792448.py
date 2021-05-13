h,w=map(int,input().split())
s=["."*(w+2)]
for i in range(h):
    S="."+input()+"."
    s.append(S)
s.append("."*(w+2))
for i in range(1,h+1):
    ans=[]
    for j in range(1,w+1):
        cnt=0
        if s[i][j]==".":
            if s[i-1][j-1]=="#":
                cnt+=1
            if s[i-1][j]=="#":
                cnt+=1
            if s[i-1][j+1]=="#":
                cnt+=1
            if s[i][j-1]=="#":
                cnt+=1
            if s[i][j+1]=="#":
                cnt+=1
            if s[i+1][j-1]=="#":
                cnt+=1
            if s[i+1][j]=="#":
                cnt+=1
            if s[i+1][j+1]=="#":
                cnt+=1
            ans.append(str(cnt))
        else:
            ans.append("#")
    print("".join(ans))