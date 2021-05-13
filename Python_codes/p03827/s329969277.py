N=int(input())
S=input()

x=[0]*(N+1)
for i in range(N):
    if S[i]=="I":
        x[i+1]=x[i]+1
    else:
        x[i+1]=x[i]-1
print(max(x))