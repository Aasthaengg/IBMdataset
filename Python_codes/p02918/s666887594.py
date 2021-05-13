N,K=map(int,input().split())
S=input()

H=0
cnt=0
for i in range(N):
    if i>0 and S[i]==S[i-1]=="L":
        H+=1
    elif i<N-1 and S[i]==S[i+1]=="R":
        H+=1
    if i<N-1 and S[i]!=S[i+1]:
        cnt+=1
print(H+min(cnt,K*2))