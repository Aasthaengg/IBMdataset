h,w,k=map(int,input().split())
ans=10**18
s=[input() for _ in range(h)]
for i in range(2**(h-1)):
    div=[0]
    for j in range(h-1):
        if (i>>j)&1:
            div.append(j)
    div.append(h-1)
    n=len(div)
    divcnt=[0]*(n-1)
    j=-1
    prev=-1
    cnt=n-2
    ok=True
    while 1:
        l=1
        j+=1
        if j==w:
            break
        for m in range(h):
            if m<=div[l]:
                #print(l,j,m)
                if divcnt[l-1]+int(s[m][j])>k:
                    j-=1
                    #print(prev)
                    if j==prev:
                        #print(divcnt)
                        ok=False
                    else:
                        prev=j
                        cnt+=1
                        #print(cnt)
                        divcnt=[0]*(n-1)
                    break
                else:
                    divcnt[l-1]+=int(s[m][j])
                if m==div[l]:
                    if l<n-1:
                        l+=1
                    else:
                      break
        if not ok:
            break
    if ok:
        ans=min(cnt,ans)
print(ans)