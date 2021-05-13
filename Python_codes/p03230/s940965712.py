n= int(input())
k=((8*n+1)**0.5-1)/2
if k.is_integer():
    print('Yes')
    ik=int(k)
    print(ik+1)
    prel,newl=[],[]
    nexv,last=0,0
    for i in range(ik+1):
        if i==0:
            print(ik,*[t+1 for t in range(ik)])
            nexv=1
        else:
            last+=ik-i+1
            newl=[b+last+1 for b in range(ik-i)]
            for b in range(len(prel)):prel[b]+=1
            print(ik,*(prel+[nexv]+newl))
            prel.append(nexv)
            if newl:nexv=newl[0]
else:print('No')