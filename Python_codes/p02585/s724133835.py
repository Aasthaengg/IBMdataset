N,K=map(int,input().split())
P=[0]+list(map(int,input().split()))
C=[0]+list(map(int,input().split()))
D=[0 for i in range(N+1)]
D[0]=5

ans=-10**20
for i in range(1,N+1):
    if D[i]==0:
        D[i]=1
        p=P[i]
        cnt=-10**20
        L=[0]
        l=[i]
        for j in range(10**7):
            if D[p]==5:
                break
            else:
                D[p]+=1
                L.append(L[-1]+C[p])
                l.append(p)
                p=P[p]
        #print(L)
        #print(l)
        loop_len=len(L)//5
        loop_cnt=L[loop_len]
        #print(loop_len)
        #print(loop_cnt)
        R=K//loop_len
        M=K%loop_len
        loop_max=-10**20
        if R>=2 and loop_cnt>0:
            cnt+=(R-2)*loop_cnt
            for x in range(loop_len):
                for y in range(1,M+2*loop_len+1):
                    loop_max=max(loop_max,L[y+x]-L[x])
            cnt=max(cnt,loop_cnt*(R-2)+loop_max)
            #print(L,cnt)
            ans=max(ans,cnt)
        else:
            cnt=-10**20
            for x in range(loop_len):
                for y in range(1,min(K,2*loop_len)+1):
                    cnt=max(cnt,L[y+x]-L[x])
                    #print(L,cnt,x,y,R)
            ans=max(ans,cnt)
#print(D)
print(ans)