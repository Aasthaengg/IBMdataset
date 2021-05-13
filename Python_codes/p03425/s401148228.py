n=int(input())
march="MARCH"
c=[0 for _ in range(5)]
for i in range(n):
    s=str(input())
    for j in range(5):
        if s[0]==march[j]:
            c[j]+=1

ans=0
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            ans+=c[i]*c[j]*c[k]
print(ans)