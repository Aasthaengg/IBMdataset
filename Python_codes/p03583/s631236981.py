N=int(input())
a=4/N
h_st=max(int(N*(1/4))-1,1)
#h_st=1
for h in range(h_st,3501):
    H=1/h
    for n in range(h,3501):
        flag=0
        if 4*h*n*n-(n*n+h*n+h*n)*N<=0 and 4*h*n*3500-(n*3500+h*3500+h*n)*N>=0:

            st,end=n,3500
            for w in [st,end]:
                B=4*h*n*w-(n*w+h*w+h*n)*N
                if B==0:
                    flag=1
                    break
            while st!=end:
                #print(h,n,st,end)
                w=int((st+end)/2)
                if end-st==1:
                    end=w
                    st=w
                B=4*h*n*w-(n*w+h*w+h*n)*N
                if B==0:
                    flag=1
                    break
                elif B>0:
                    end=w
                else:
                    st=w

        if flag:
            break
    if flag:
        break

print(h,n,w)
