T1,T2 = map(int,input().split())
A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())
dif = T1*A1+T2*A2-T1*B1-T2*B2
if dif==0:
    print("infinity")
elif dif>0:
    if B1>A1:
        k = int(((B1-A1)*T1)/dif)
        if abs(((B1-A1)*T1)/dif-round(((B1-A1)*T1)/dif))<1e-20:
            print(2*round(((B1-A1)*T1)/dif))
        else:
            print(2*k+1)
    else:
        print(0)
else:
    if A1>B1:
        k = int(((A1-B1)*T1)/abs(dif))
        if abs((A1-B1)*T1/abs(dif)-round(((A1-B1)*T1)/abs(dif)))<1e-20:
            print(2*round(((A1-B1)*T1)/abs(dif)))
        else:
            print(2*k+1)
    else:
        print(0)