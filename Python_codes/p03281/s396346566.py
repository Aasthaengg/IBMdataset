n=int(input())

a=[]
for i in range(1,201):
    s=0
    for j in range(1,int(i**0.5)+1):
        if i%j==0:
            s+=1
            if j != i//j:
                s+=1
    a.append(s)

ans=0
for i in range(n):
    if a[i]==8 and i%2==0:
        ans+=1

print(ans)