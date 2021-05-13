N=int(input())
X=list(map(int,input().split()))


pdlist=[]

for i in range(101):
    pd=0
    for j in X:
        pd+=(i-j)**2
    pdlist.append(pd)
    
pdlist.sort()
print(pdlist[0])
