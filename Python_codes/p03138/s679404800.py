#117_D
N,K=map(int,input().split())
A=list(map(int,input().split()))
#各桁の和を求める
Pro=[0]*40
for i in range(40):
    res=0
    for j in range(N):
        if (A[j]>>i)&1:
            res+=1
    Pro[i]=res

K_bin=[]
tmp=K+1
for i in range(40):
    K_bin.append(tmp%2)
    tmp//=2
    
Ans=0    
    
for i in range(40):
    x=0
    if K_bin[i]==1:
        x+=sum([max(Pro[j],N-Pro[j])*(2**j) for j in range(0,i)])
        x+=Pro[i]*(2**i)
        x+=sum([(2**j)*(Pro[j]+(N-2*Pro[j])*K_bin[j]) for j in range(i+1,40)])
    Ans=max(Ans,x)
    
print(Ans)