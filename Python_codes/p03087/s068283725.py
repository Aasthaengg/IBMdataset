n,q=map(int,input().split())
st=input()
ssum=[0,0]
for i in range(1,n):
    if st[i-1]=="A" and st[i]=='C':
        ssum.append(ssum[-1]+1)
    else:
        ssum.append(ssum[-1])
#print(len(ssum))
for i in range(q):
    a,b=map(int,input().split())
    print(ssum[b]-ssum[a])