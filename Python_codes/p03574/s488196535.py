h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(list(input()))
a=["+" for i in range(w)]
s.append(a)
s.insert(0,a)
for i in range(h+2):
    s[i].append("+")
    s[i].insert(0,"+")
for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j]==".":
            m=0
            for x in range(3):
                for y in range(3):
                    if s[i-1+x][j-1+y]=="#":
                        m+=1
            s[i][j]=str(m)
for i in range(1,h+1):
    ans=s[i][1]
    for j in range(w-1):
        ans=ans+s[i][j+2]
    print(ans)
