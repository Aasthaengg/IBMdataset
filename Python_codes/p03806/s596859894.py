n,ma,mb=map(int,input().split())
zen=[[10**10]*401 for i in range(401)]
kou=[[10**10]*401 for j in range(401)]
A=[ list(map(int,input().split())) for i in range(n//2)];a=len(A)
B=[ list(map(int,input().split())) for i in range(n-n//2)];b=len(B)
for bit in range(1<<a):
    now=[0,0,0]
    for i in range(a):
        if (bit>>i)&1:
            now[0]+=A[i][0]
            now[1]+=A[i][1]
            now[2]+=A[i][2]
    zen[now[0]][now[1]]=min(zen[now[0]][now[1]],now[2])
for bit in range(1<<b):
    now=[0,0,0]
    for i in range(b):
        if (bit>>i)&1:
            now[0]+=B[i][0]
            now[1]+=B[i][1]
            now[2]+=B[i][2]
    kou[now[0]][now[1]]=min(kou[now[0]][now[1]],now[2])


ans=10**10
for base in range(1,401):
    na=base*ma ; nb=base*mb 
    if max(na,nb)>400: break
    for i in range(na+1):
        for j in range(nb+1):
            ans=min(ans,zen[i][j]+ kou[na-i][nb-j])


print(ans if ans<10**6 else -1)