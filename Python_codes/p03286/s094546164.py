n=int(input())
ans=""
i=0
if n==0:
    print(0)
    exit()

while n!=0 :
    if n%2==0:
        ans+="0"

    else:
        ans+="1"
        if i%2==0:
            n-=1
        else:
            n+=1
    n=n//2
    i+=1
    #print(n,ans)

print(ans[::-1])