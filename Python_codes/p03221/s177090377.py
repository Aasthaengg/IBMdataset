n,m=map(int,input().split())
d={i:[] for i in range(1,n+1)}
a=['' for i in range(m)]
for i in range(1,m+1):
    p,y=map(int,input().split())
    d[p].append([i,y])
#print(d)
for p,j in d.items():
    j.sort(key=lambda x:x[1])
    for i in range(len(j)):
        a[j[i][0]-1]=format(p,'0>6')+format(i+1,'0>6')
print(*a,sep='\n')