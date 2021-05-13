k,a,b=map(int,input().split())

if a+1<b:
    ans=0
    if k<=a:
        ans=k+1
    else:
        ans=(a-1)+1
        k-=(a-1)
        if k%2==0:
            #print("even")
            ans+=(k//2)*(b-a)
        else:
            #print("odd")
            ans+=(k//2)*(b-a)+1


    print(ans)


else:
    print(1+k)
