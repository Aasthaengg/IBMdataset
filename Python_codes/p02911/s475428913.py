N,K,Q=map(int,input().split())

if Q-K>=0:
    lis=[0]*N
    lis_yn=['No']*N
    for _ in range(Q):
        q=int(input())
        lis[q-1]+=1
        if lis[q-1]>Q-K:
            lis_yn[q-1]='Yes'
    #print(lis)
else:
    lis_yn=['Yes']*N
print('\n'.join(lis_yn))
