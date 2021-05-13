N,K=map(int,input().split())
l=[0]*K
for i in range(1,N+1):
    l[i%K]+=1
l.sort(key=int)
print(abs(l[0]-l[-1]))