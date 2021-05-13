N,Y=map(int,input().split())
flag=0
ten_key=int(Y/10000)
one_key=int(Y/1000)
if N<ten_key or one_key<N:
    print(-1,-1,-1)

else:
    amari=Y-(ten_key*10000)
    five_key=int(amari/5000)
    if N-ten_key<five_key:
        print(-1,-1,-1)
    
    else:
        for i in range(ten_key+1):
            if flag==1:
                break
            amari=Y-(i*10000)
            five_key=int(amari/5000)
            for j in range(five_key+1):
                one_max=N-i-j
                amari=Y-((i*10000)+(j*5000))
                one_key=int(amari/1000)
                if one_key+i+j==N:
                    print(i,j,one_key)
                    flag=1
                    break
        if flag==0:
            print(-1,-1,-1)
