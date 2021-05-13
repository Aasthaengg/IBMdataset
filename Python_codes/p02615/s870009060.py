N=int(input())
A=list(map(int,input().split()))
B=sorted(A,reverse=True)
S=0
i=0
for j in range(1,N):
    if j%2==1:
        S+=B[i]
        i+=1
    else:
        S+=B[i]
print(S)