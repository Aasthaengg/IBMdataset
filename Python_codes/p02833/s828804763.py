n=int(input())

if n%2==1:
    print(0)
else:
    ans=0
    i=10
    while (n//i !=0):
        ans+=(n//i)
        i*=5
    print(ans)



