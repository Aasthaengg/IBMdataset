n,q=map(int,input().split())
nextlist=[[] for _ in range(n)]
pointlist=[0]*n
for i in range(n-1):
    tmpa,tmpb=map(int,input().split())
    nextlist[tmpa-1].append(tmpb)
    nextlist[tmpb-1].append(tmpa)

for i in range(q):
    tmpp,tmpx=map(int,input().split())
    pointlist[tmpp-1] += tmpx

#for i,next in enumerate(nextlist):
#    next.append(pointlist[i])
outlist=[0]*n
done=[False]*n
nextp=[[],[]]

outlist[0]=pointlist[0]
done[0]=True
for j in nextlist[0]:
    nextp[0].append([j,pointlist[0]])
    done[j-1]=True

i=0

while True:
    x = -i+1
    if nextp[i] == []:
        break
    else:
        for ne in nextp[i]:
            n=ne[0]
            p=ne[1]
            outlist[n-1] = pointlist[n-1] + p

            for j in nextlist[n-1]:
                if not done[j-1]:
                    nextp[x].append([j,outlist[n-1]])
                    done[j-1]=True
        nextp[i]=[]
        i=x

for out in outlist:
    print(out,end=' ')