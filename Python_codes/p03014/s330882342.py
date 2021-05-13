h,w=map(int,input().split())
s=[input() for ri in range(h)]
table=[0]*(h*w)
for i in range(h):
    p=0
    pre=0
    for j in range(w):
        if s[i][j]=="#":
            if p==0:continue
            for x in range(pre,j):
                table[w*i+x]+=p
            p=0
        else:
            if p==0:
                pre=j
            p+=1
    else:
        if p:
            for x in range(pre,w):table[w*i+x]+=p

for j in range(w):
    p=0
    pre=0
    for i in range(h):
        if s[i][j]=="#":
            if p==0:continue
            for x in range(pre,i):
                table[j+w*x]+=p
            p=0
        else:
            if p==0:pre=i
            p+=1
    else:
        if p:
            for x in range(pre,h):table[j+w*x]+=p
        p=0

print(max(table)-1)