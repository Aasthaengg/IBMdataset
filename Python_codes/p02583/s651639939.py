N=int(input())
L=list(map(int,input().split()))
L=sorted(L)
count=0
if N==1 and N==2:
    print(0)
else:
    for i in range(N-2):
        for j in range(i+1,N-1):
            if L[i]!=L[j]:
                for k in range(j+1,N):
                    if L[j]<L[k] and L[k]<L[i]+L[j]:
                        count+=1
    print(count)