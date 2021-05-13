h,w=map(int,input().split())

s=[]
s.append("."*(w+2))
for i in range(h):
    s.append("."+input()+".")
s.append("."*(w+2))

#print(s)
k=[]
for i in range(h):
    p=[]
    for j in range(w):
        cnt=0
        if s[i+1][j+1]==".":
            if s[i][j]=="#":
                cnt+=1
            if s[i][j+1]=="#":
                cnt+=1
            if s[i][j+2]=="#":
                cnt+=1
            if s[i+1][j]=="#":
                cnt+=1
            if s[i+1][j+2]=="#":
                cnt+=1
            if s[i+2][j]=="#":
                cnt+=1
            if s[i+2][j+1]=="#":
                cnt+=1
            if s[i+2][j+2]=="#":
                cnt+=1
            p.append(cnt)
        else:
            p.append("#")
    k.append(p)
    
for i in range(h):
    for j in range(w):
        print(k[i][j],end="")
    print()
    
        
