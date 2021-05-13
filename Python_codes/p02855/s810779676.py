h,w,k=map(int,input().split())
s=[input()for _ in range(h)]
ki=0
ans=[]
ansi=''
for i in range(h):
    if s[i].count('#')>1:
        b=[n for n,v in enumerate(s[i]) if v=='#']
        b.append(w)
        ki+=1
        ansi=(' '+str(ki))*b[1]
        for l in range(2,len(b)):
            ki+=1
            ansi+=(' '+str(ki))*(b[l]-b[l-1])
        while len(ans)<i+1:
            ans.append(ansi)
    elif s[i].count('#')==1:
        ki+=1
        ansi=(' '+str(ki))*w
        while len(ans)<i+1:
            ans.append(ansi)
while len(ans)<h:
    ans.append(ansi)
for ai in ans:
    print(ai[1:])
