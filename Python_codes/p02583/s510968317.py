N=int(input())
L=[int(i) for i in input().split()]

count=0
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if (L[i]!=L[j])&(L[i]!=L[k])&(L[j]!=L[k]):
                if (L[i]+L[j]>L[k])&(L[i]+L[k]>L[j])&(L[j]+L[k]>L[i]):
                    count+=1
print(count)