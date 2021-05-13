s=int(input())
a=[s]
i=0
while True:
    if a[i]%2==0:
        temp=a[i]//2
        if temp in a:
            ans=i+2
            break
        a.append(temp)
    else:
        temp=3*a[i]+1
        if temp in a:
            ans=i+2
            break
        a.append(temp)
    i+=1

print(ans)