N,K=map(int,input().split())
S=[0]*N
b=0

for i in range(K):
    d=input()
    A=list(map(int,input().split()))
    for j in A:
        S[j-1]+=1

for i in range(len(S)):
    if S[i]==0:
        b+=1
print(b)