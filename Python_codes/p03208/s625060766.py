N,K=map(int,input().split())
S=[]
for i in range(N):
    S.append(int(input()))

S.sort()
minh=10**10
for i in range(N-K+1):
    if minh>S[i+K-1]-S[i]:
        minh=S[i+K-1]-S[i]

print(minh)
    
