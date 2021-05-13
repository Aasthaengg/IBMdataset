N=int(input())
L=sorted(list(map(int,input().split())))

c=0
for i in range(N-2):
    for j in range(i+1,N-1):
        if L[i]==L[j]:
            continue
        for k in range(j+1,N):
            if L[j]==L[k]:
                continue
            if L[i]+L[j]>L[k]:
                c+=1
            else:
                break
print(c)
