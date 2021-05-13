N,C,K=map(int,input().split())
T=[int(input()) for _ in range(N)]
T.sort()
#print(T)
if C==1:
    print(N)
    exit()
ans=0
i=0
j=1
tmp=1
while True:
    #print(i,j)
    if j-i==C:
        if j==N:
            ans+=1
            break
        ans+=1
        i=j
        j=i+1
        tmp=1
    if j>=N:
        ans+=1
        break
    if i!=N-1:
        if T[j]-T[i]>K:
            ans+=1
            i=j
            j=i+1
            tmp=1
            continue
        else:
            j+=1
            tmp+=1
print(ans)