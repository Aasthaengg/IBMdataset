S=list(map(int,input()))
s=len(S)
if s==1:
    print(S[0])
else:

    s=s-1
    t=pow(2,s)
    l=len(list(format(t-1,'b')))
    x=0
    for i in range(t):
        k=list(format(i,'b'))
        L=[0]*l
        x+=S[-1]
        v=1
        for i in range(l):
            if i+1<=len(k):
                L[l-i-1]=k[-1-i]
            if int(L[l-i-1])==0:
                v=v*10
                x+=v*S[len(S)-2-i]
            else:
                v=1
                x+=S[len(S)-2-i]
    print(x)

        
        


