N,K = list(map(int,input().split()))
n=(N-K)//(K-1)+1
mod=(N-K)%(K-1)
if mod!=0:
    n+=1

print(n)