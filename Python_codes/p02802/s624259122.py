n,m=map(int,input().split())
p=[0]*m
s=[0]*m
for i in range(m):
    pi,si=input().split()
    p[i]=int(pi)
    s[i]=si
judge=[0]*(n+1)
ac=0
wa=0
for i in range(m):
    if judge[p[i]]==-1:
        continue
    if judge[p[i]]!=-1:
        if s[i]=='WA':
            judge[p[i]]+=1
        else:
            wa+=judge[p[i]]
            judge[p[i]]=-1
            ac+=1
print(ac,wa)