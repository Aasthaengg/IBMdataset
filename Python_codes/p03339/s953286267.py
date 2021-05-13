N = int(input())
S = input()

E = [0]*(N+1)
W = [0]*(N+1)

for i in range(N):
    if S[i] == "E":
        E[i+1] = E[i] + 1
        W[i+1] = W[i]
    else:
        E[i+1] = E[i]
        W[i+1] = W[i] + 1

min = N

for i in range(N):
    S = W[i]-W[0] + E[N]-E[i+1]
    if S < min:
        min = S
    
print(min)