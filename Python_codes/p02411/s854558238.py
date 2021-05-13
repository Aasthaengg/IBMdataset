N=int(0)
i=int(0)
m,f,r,point=[],[],[],[]
while 1:
    point=list(map(int,input().split(' ')))
    m.append(point[0])
    f.append(point[1])
    r.append(point[2])
    if(m[i]==-1&f[i]==-1&r[i]==-1):
        break
    N=N+1
    i=i+1
i=0
while (i<N):
    if(m[i]+f[i]>=80 and m[i]!=-1 and f[i]!=-1):
        print('A')
    elif(m[i]+f[i]>=65 and m[i]+f[i]<80 and m[i]!=-1 and f[i]!=-1):
        print('B')
    elif(m[i]+f[i]>=50 and m[i]+f[i]<65 and m[i]!=-1 and f[i]!=-1):
        print('C')
    elif(m[i]+f[i]>=30 and m[i]+f[i]<50 and m[i]!=-1 and f[i]!=-1):
        if(r[i]>=50):
            print('C')
        else:
            print('D')
    elif(m[i]+f[i]<30 or m[i]==-1 or f[i]==-1):
        print('F')
    i=i+1
