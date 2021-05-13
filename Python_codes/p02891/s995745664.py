S=input()
K=int(input())

L=len(S)

D=[0]*(2*L)

D[0]=1
n=0
for i in range(1,2*L):
    if S[(i-1)%L]==S[i%L]:
        D[i]=D[i-1]+1
        n+=1
    else:
        D[i]=1

X=[]
if D[L-1]==L:
        print((L*K)//2)
else:
    if S[0]==S[-1]:
        f,g=True,False

        i=0
        while f:
            g=g or (S[i]!=S[i+1])
            
            if D[i]>=D[i+1]:
                if g:
                    X.append(D[i])
                    if i>=L-1:
                        f=False
                        
            i+=1

        A=sum(map(lambda n:n//2,X[1:]))*(K-1)+sum(map(lambda n:n//2,X[1:-1]))+(X[0]//2)+(D[L-1]//2)
    
    else:
        for i in range(L):
            if D[i]>D[i+1]:
                X.append(D[i])


        A=sum(map(lambda n:n//2,X))*K

    print(A)
