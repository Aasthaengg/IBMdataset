n=int(input())
ans=0
for i in range(1,n+1):
    i2 = str(i)
    if int(i2[-1])==0:
        pass
    elif int(i2[0]) > int(i2[-1]):
        for j in range(len(i2)-1):
            ans+= (10**j)*2
    elif int(i2[0]) < int(i2[-1]):
        for j in range(len(i2)-2):
            ans+= (10**j)*2
    elif len(i2)>2:
        for j in range(len(i2)-2):
            ans+= (10**j)*2
        ans+=3
        ans+=int(i2[1:-1])*2
    else:
        ans+=len(i2)*2-1
print(ans)