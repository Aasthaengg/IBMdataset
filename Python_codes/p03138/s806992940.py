N,K=map(int,input().split())
A=list(map(int,input().split()))
d=[0 for _ in range(40)]
att=[[0,i] for i in range(40)]
x=0
s=sum(A)
num=0
for i in range(N):
    x=A[i]
    for j in range(40):
        if (x>>j)&1:
            d[j]=d[j]+1
#print(d)
for i in range(40):
    att[i][0]=(N-2*d[i])*pow(2,i)
att.sort(key=lambda x:x[0],reverse=True)
#print(att,s)
for i in range(40):
    if (att[i][0]>0)and(num+pow(2,att[i][1])<=K):
        s=s+att[i][0]
        num=num+pow(2,att[i][1])
print(s)
