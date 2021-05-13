N=int(input())
L=list(map(int,input().split()))
L.sort()
ans=0
for i in range(len(L)):
    a=L[i]
    for j in range(i+1,len(L)):
        if L[j]!=a:
            b=L[j]
            for k in range(j+1,len(L)):
                if L[k]!=b:
                    if a+b>L[k]:
                        ans+=1
                    else:
                        break
print(ans)
