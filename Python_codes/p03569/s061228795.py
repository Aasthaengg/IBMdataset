s=input()
t=s.replace('x','')
if t!=t[::-1]:
    print(-1)
else:
    l=[]
    k=0
    for c in s:
        if c=='x':
            k+=1
        else:
            l.append(k)
            k=0
    l.append(k)

    ans=0
    for i in range(len(l)//2):
        ans+=abs(l[i]-l[-(i+1)])

    print(ans)