T1,T2=map(int,input().split())
A1,A2=map(int,input().split())
B1,B2=map(int,input().split())

if A1<B1:
    A1,B1=B1,A1
    A2,B2=B2,A2

if A2>=B2:
    print(0)
else:
    sta=T1*(A1-B1)
    gen=T2*(A2-B2)
    if sta==-gen:
        print("infinity")
    elif sta+gen>0:
        print(0)        
    else:
        ans=sta//abs(sta+gen)*2+1
        if sta%abs(sta+gen)==0:
            ans-=1
        print(ans)