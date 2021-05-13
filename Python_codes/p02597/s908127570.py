N= int(input())
c=list(str(input()))
#N=4
#c=['W', 'W', 'R', 'R']
#c.reverse()
#print(c)

t1=t2=True

n1=0
n2=0
num=0
while t1:
    t2=True
    if not 0<=N-1-n1<=N-1:
        t1=False
    if c[N-1-n1]=='W':
        n1+=1
        continue
    else:
        while t2:
            if c[n2]=='W':
                if n2<N-1-n1:
                    c[N-1-n1]='W'
                    c[n2]='R'
                    num+=1
                    t2=False
                    continue
                else:
                    t1=False 
            n2+=1
            if not 0<=n2<=N-1:
                t1=False
                t2=False
print(num)  