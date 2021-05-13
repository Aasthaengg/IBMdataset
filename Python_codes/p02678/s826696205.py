n,m=map(int,input().split())
s=[[]for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    s[a-1].append(b-1)
    s[b-1].append(a-1)
t=[-1]*n
q=[0]
while q:
    p=[]
    for j in q:
        for i in s[j]:
            if i!=j and t[i]==-1:
                p.append(i)
                t[i]=j
    q=p[::]
print("Yes")
for i in t[1:]:
    print(i+1)