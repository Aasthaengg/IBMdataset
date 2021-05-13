n=int(input())
lst=list(map(int,input().split()))
anslst=[None]*n
for i in range(n,0,-1):
    amari=lst[i-1]
    tmp=i*2
    kosuu=0
    while tmp-1<n:
        if anslst[tmp-1]==1:
            kosuu+=1
        tmp+=i
    kosuu%=2
    if kosuu==amari:
        anslst[i-1]=0
    else:
        anslst[i-1]=1
cnt=0
ans=[]
for i in range(n):
    if anslst[i]==1:
        cnt+=1
        ans.append(i+1)
print(cnt)
print(*ans)