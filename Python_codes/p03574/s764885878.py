h,w = map(int,input().split())
s =["."*(w+2)]+["."+input()+"." for i in range(h)]+["."*(w+2)]

for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j] !="#":
            a=s[i][j-1]+s[i][j+1]+s[i-1][j-1:j+2]+s[i+1][j-1:j+2]
            s[i]=s[i][:j]+str(a.count("#"))+s[i][j+1:]

[print(s[i][1:w+1]) for i in range(1,h+1)]
