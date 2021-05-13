a,b,c=map(int,input().split())
ans=0
if a%2==0 and b%2==0 and c%2==0 and a==b and b==c:
    print(-1)
else:
    while True:
        if a%2==0 and b%2==0 and c%2==0:
            ans+=1
            a_tmp=int(a/2)
            b_tmp=int(b/2)
            c_tmp=int(c/2)
            a=b_tmp+c_tmp
            b=a_tmp+c_tmp
            c=b_tmp+b_tmp
        else:
            break
    print(ans)