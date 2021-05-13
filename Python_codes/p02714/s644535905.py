N = int(input())
S = list(input())
R = [0]*N
G = [0]*N
B = [0]*N
for i in range(N):
    if S[i]=="R":
        R[i] += 1
    elif S[i] == "G":
        G[i] += 1
    else:
        B[i] += 1

ans = sum(R)*sum(G)*sum(B)

for i in range(N):
    for j in range(i+1,min((N+i+3)//2,N)):
        k = 2*j-i
        if  k<N:
            if S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]:
                ans -= 1
                
print(ans)