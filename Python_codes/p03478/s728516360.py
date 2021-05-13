N,A,B=map(int,input().split())
tt=0
for i in range(N+1):
    ans=0
    temp=str(i)
    for j in range(len(temp)):
        ans+=int(temp[j])
    if A<=ans and ans<=B:
        tt+=int(temp)

print(tt)