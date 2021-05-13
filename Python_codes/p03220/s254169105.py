N=int(input())
T,A=map(int,input().split())
H=[-1000]+list(map(int,input().split()))


M=10**10
X=0
for i in range(1,N+1):
    B=abs(1000*(T-A)-6*H[i])
    if B<=M:
        M=B
        X=i
print(X)
    
