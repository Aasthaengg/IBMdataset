n, a, b, c=map(int, input().split())
l=[0]*n
ch=0
ans=0

for i in range(n):
    l[i]=int(input())

ans+=abs(l[0]-a)
ans+=abs(l[1]-b)
ans+=abs(l[2]-c)

    
for i in range(4**n):
    ch=0
    mp=0
    s=[0]*4
    for j in range(n):
        for k in range(3):
            if (i>>2*j) % 2**2 ==k:
                if s[k]==0:
                    0
                else:
                    mp+=10
                s[k]+=l[j]
                    
    for p in range(3):
        if s[p]==0:
            #invalid
            ch=1
    if ch==1:
        0
        #invalid
    else:
        mp+=abs(int(s[0]-a))
        mp+=abs(int(s[1]-b))
        mp+=abs(int(s[2]-c))
        if mp<ans:
            ans=mp
            s_ans=s
            j_ans=j
    #print('bin(j),ch,s,mp',bin(i),ch,s,mp,abs(int(s[0]-a)),abs(int(s[1]-b)),abs(int(s[2]-c)))
    
print(ans)
#print(bin(j_ans),s_ans)
    
    
