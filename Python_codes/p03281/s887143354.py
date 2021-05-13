n=int(input())
ans=0
o=[a for a in range(1,n+1) if a%2==1]
for i in o:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==8:
        ans+=1
print(ans)