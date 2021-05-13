n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort()
l.append([-1,-1])
a=[]
b=[]
for i in range(n):
    if l[i][0]==l[i+1][0]:
        b.append(l[i][1])
    else:
        a.append(l[i][1])
ans=len(a)*len(a)+sum(a)
#print(ans)
if len(b)>0:
    ans+=sum(b)
    b.sort()
    a.sort()
    i=0
    ai=0
    bi=0
    an=len(a)
    bn=len(b)
    while i<n-k:
        if ai<an and bi<bn:
            ap=a[ai]
            bp=b[bi]
            if ap+2*(an-ai-1)+1>=bp:
                bi+=1
                ans-=bp
            else:
                ans-=ap+2*(an-ai-1)+1
                ai+=1
        elif ai<an:
            ap=a[ai]
            ans-=ap+2*(an-ai-1)+1
            ai+=1
        elif bi<bn:
            ans-=b[bi]
            bi+=1
        i+=1
    print(ans)
else:
    a.sort(reverse=True)
    print(sum(a[:k])+k*k)
