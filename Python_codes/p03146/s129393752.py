a=int(input())
if a==1:
    print(4)
    exit()
elif a==4:
    print(4)
    exit()
elif a==2:
    print(4)
    exit()

ans=1
while True:
    if a==4:
        break
    elif a%2==0:
        a=a/2
        ans+=1
    else:
        a=3*a+1
        ans+=1

print(ans+3)