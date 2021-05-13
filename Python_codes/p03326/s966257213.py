import itertools
N,M=map(int,input().split())
tributes=[]
ans=0
seq=(0,1,2)
for i in range(N):
    x,y,z=map(int,input().split())
    tributes.append([x,y,z])
for i in range(8):
    sor=[0]*3
    for j in range(3):
        if (i >> j) & 1:
            sor[j] = 1
    l=[]
    for i in range(N):
        num=0
        for j in range(3):
            num=num+tributes[i][j]*pow(-1,sor[j])
        l.append(num)
    l.sort(reverse=True)
    ans=max(ans,sum(l[:M]))
print(ans)

"""
order=list(itertools.permutations(seq))
#print(ord)

for i in range(len(order)):
    for j in range(8):
        sor=[0]*3
        l=[0]*3
        for k in range(3):
            if (j>>k)&1:
                sor[k]=1
        for k in range(3):
            if sor[k]==0:
                if k!=2:
                    tributes=sorted(tributes,key=lambda x:x[order[i][k]])
                else:
                    tributes.sort(key=lambda x:x[order[i][k]])
            else:
                if k!=2:
                    tributes=sorted(tributes,key=lambda x:x[order[i][k]],reverse=True)
                else:
                    tributes.sort(key=lambda x:x[order[i][k]],reverse=True)
        for k in range(M):
            l[0] = l[0] + tributes[k][0]
            l[1] = l[1] + tributes[k][1]
            l[2] = l[2] + tributes[k][2]
        l=list(map(lambda x:abs(x),l))
        ans=max(ans,sum(l))
print(ans)

#2→1→0
tributes=sorted(tributes,key=lambda x:x[2])
tributes=sorted(tributes,key=lambda x:x[1])
tributes.sort(key=lambda x:x[0])
#print(tributes)
l=[0]*3
for i in range(M):
    l[0]=l[0]+tributes[i][0]
    l[1] = l[1] + tributes[i][1]
    l[2] = l[2] + tributes[i][2]
l=list(map(lambda x:abs(x),l))
ans=max(ans,sum(l))
"""

