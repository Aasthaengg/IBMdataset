N=int(input())
ans=0
for i in range(N+1):
    if i>1 and i%2==1:
        div=[1,i]
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                div.append(j)
                div.append(i//j)
        if len(div)==8:
            ans+=1
print(ans)