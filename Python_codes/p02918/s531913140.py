N,K=map(int,input().split())
S=str(input())
section=0
for i in range(N-1):
    if S[i]==S[i+1]:
        continue
    else:
        section+=1
print(N-max(0,section-2*K)-1)
