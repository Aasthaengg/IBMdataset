# ABC140 D
N,K=map(int,input().split())
S=input()

s=''
happy=0
for i in range(N):
    if s==S[i]:
        happy+=1
    s=S[i]
print(min(happy+2*K,N-1))