N,K=map(int,input().split())
S=list(map(str,input()))

S[K-1]=S[K-1].lower()

for i in range(N):
    print(S[i],end="")