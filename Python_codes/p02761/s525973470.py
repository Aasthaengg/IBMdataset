n,m = map(int,input().split())

r = []
ans = -2

for i in range(n):
    r.append(-1)

# n>1
if n>1:
    for i in range(m):
        s, c = map(int,input().split())
        s=s-1
        if s==0 and c==0: 
            ans = -1
        elif r[s]!=-1 and r[s]!=c:
            ans = -1
        else:
            r[s]=c

#n=1

if n==1:
    for i in range(m):
        s, c = map(int,input().split())
        s=s-1
        if r[s]!=-1 and r[s]!=c:
            ans = -1
        else:
            r[s]=c

if ans==-1:
    print(ans)
else:
    for i in range(n):
        if i==0 and r[i]==-1:
            if n!=1:
                r[i]=1
            else:
                r[i]=0
        if i!=0 and r[i]==-1:
            r[i]=0
        r[i]=str(r[i])
    print(''.join(r))


