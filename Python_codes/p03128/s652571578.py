N,M=map(int,input().split())
A=list(map(int,input().split()))
d={2:0,3:0,4:0,5:0,6:0,7:0}
for i in A:
    if i==1:
        d[2]=1
    elif i==7:
        d[3]=7
    elif i==8:
        d[7]=8
    elif i==4:
        d[4]=4
    elif i==6 or i==9:
        if d[6]<i:
            d[6]=i
    else:
        if d[5]<i:
            d[5]=i
l=[]
for i in d.keys():
    if d[i]:
        l.append(i)
l.sort()
a=[]
m=0
if len(l)>=4:
    for i in range(4):
        for j in range(4):
            for k in range(4):
                t=N-i*l[1]-j*l[2]-k*l[3]
                if t%l[0] or t<0:
                    continue
                ke=i+j+k+t//l[0]
                if ke<m:
                    continue
                else:
                    s=[d[l[1]]]*i+[d[l[2]]]*j+[d[l[3]]]*k+[d[l[0]]]*(t//l[0])
                    s.sort(reverse=1)
                    if ke==m:
                        a.append(s)
                    else:
                        a=[s]
                        m=ke
    print(*max(a),sep="")
elif len(l)==3:
    for i in range(5):
        for j in range(5):
            t=(N-i*l[1]-j*l[2])
            if t%l[0] or t<0:
                continue
            ke=i+j+t//l[0]
            if ke<m:
                continue
            else:
                s=[d[l[1]]]*i+[d[l[2]]]*j+[d[l[0]]]*(t//l[0])
                s.sort(reverse=1)
                if ke==m:
                    a.append(s)
                else:
                    a=[s]
                    m=ke
    print(*max(a),sep="")
elif len(l)==2:
    for i in range(6):
        if (N-l[1]*i)%l[0]==0:
            a=[d[l[1]]]*i+[d[l[0]]]*((N-i*l[1])//l[0])
            a.sort(reverse=1)
            print(*a,sep="")
            break
else:
    a=[d[l[0]]]*(N//l[0])
    print(*a,sep="")