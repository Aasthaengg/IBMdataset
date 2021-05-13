n,m = map(int,input().split())

C={}
acc=0
wac=0
for i in range(m):
    p0,s = input().split()
    
    p = int(p0)
    if p in C :
        if C[p]!=-1:
            C[p]+=1
    else:
        C[p]=1

    if s=="AC" and C[p]!=-1:
        acc+=1
        wac+=C[p]-1
        C[p]=-1
        

print( acc, wac )