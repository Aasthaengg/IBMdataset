O=input()
E=input()
ans=[]
j=0
k=0
for i in range(len(O)+len(E)):
    if i%2==0:
        ans.append(O[k])
        k+=1
    else:
        ans.append(E[j])
        j+=1
print(*ans,sep="")