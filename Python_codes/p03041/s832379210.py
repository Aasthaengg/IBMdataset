N,K=map(int,input().split())
S=list(str(input()))

for i in range(N):
    if i == K-1:
        a=S[i].lower()
        S[i]=a
print(''.join(S))