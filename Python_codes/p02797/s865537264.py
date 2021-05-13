N,K,S=map(int,input().split())

ans=[]

for _ in range(K):
    print(S,end=" ")
for _ in range(N-K):
    if S!=1:
        print(S-1,end=" ")
    else:
        print(2,end=" ")

