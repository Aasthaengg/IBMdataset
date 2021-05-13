N=int(input())
a=list(map(int,input().split()))
l=[]
buf=[]
for i in range(N):
    buf=[a[i],i+1]
    buf.sort()
    l.append(buf[0]*N+buf[1])
print(len(l)-len(set(l)))

