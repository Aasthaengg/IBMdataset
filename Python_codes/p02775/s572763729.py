n=input()
l=len(n)
pre=[0,1]
for i in range(l):
    c=[0,0]
    d=int(n[i])
    c[0]=min(pre[0]+d,pre[1]+10-d)
    c[1]=min(pre[0]+d+1,pre[1]+10-d-1)
    pre=c
print(pre[0])