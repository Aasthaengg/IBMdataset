N,K=map(int,input().strip().split())
A=list(map(int,input().strip().split()))

i=A.index(1)+1
if i<=K or i>=N-K:
    ans=(N-K)//(K-1)+1 if (N-K)%(K-1)==0 else (N-K)//(K-1)+2
else:
    for a in range(K):
        if (i-a)%(K-1)==0 and (N-(i+(K-a)))%(K-1)==0:
            b=0
        else:
            b=1
    front=i//(K-1)
    back=(N-(i+K))//(K-1)
    ans=front+back+1+b
print(ans)