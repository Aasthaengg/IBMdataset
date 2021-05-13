S=input()
N=len(S)
goukei=0
for i in range(2 **(N-1)):
    T=[]
    T.append(S[0])
    for j in range(N-1):
        if ((i >> j) & 1):
            #print(i,j)のjbitがONの意味
            #print(i,j)
            T.append("+")
            T.append(S[j+1])
        else:
            T.append(S[j+1])
    
    #T.append(S[N-1])
    #print(T)
    tmp=[]
    for m in T:
        if m!="+":
            tmp.append(m)
        else:
            Z=[str(a) for a in tmp]
            Z="".join(Z)
            goukei+=int(Z)
            tmp=[]
    Z=[str(a) for a in tmp]
    Z="".join(Z)
    goukei+=int(Z)
    
print(goukei)