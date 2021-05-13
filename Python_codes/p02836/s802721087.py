S=input()
N=len(S)

K=0
for i in range(N//2):
    K+=(S[i]!=S[-(i+1)])
print(K)