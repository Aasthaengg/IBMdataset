n=int(input())
A=[int(input()) for _ in range(n)]
B={}
for i in A:
    if i in B:
        B[i]=(1+B[i])%2
    else:
        B[i]=1
print(sum(B.values()))