N,M=map(int,input().split())
a,b=[0]*M,[0]*M
for i in range(M):a[i],b[i]=map(int,input().split())
for i in range(N):print(a.count(i+1)+b.count(i+1))