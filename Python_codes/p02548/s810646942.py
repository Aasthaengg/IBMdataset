n=int(input())
ans=n-1
b=2
while True:
    a=n//b
    if n%b==0:
        a-=1
    ans+=a
    if a==0:
        break
    else:
        b+=1
        if n==b:
            break
print(ans)
