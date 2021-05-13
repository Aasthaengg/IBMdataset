N = int(input())
S = input()
R = [0]*(N+1)
G = [0]*(N+1)
B = [0]*(N+1)
for i in range(N-1, -1, -1):
    R[i] = R[i+1]+1 if S[i] == "R" else R[i+1]
    G[i] = G[i+1]+1 if S[i] == "G" else G[i+1]
    B[i] = B[i+1]+1 if S[i] == "B" else B[i+1]
ans = 0
for i in range(N):
    for j in range(i+1, N):
        if S[i] != S[j]:
            c = ["R","G","B"]
            c.remove(S[i])
            c.remove(S[j])
            c = c[0]
            if c == "R":
                ans += R[j+1]
                if 2*j-i < N and S[2*j-i] == "R":
                    ans -= 1
            if c == "G":
                ans += G[j+1]
                if 2*j-i < N and S[2*j-i] == "G":
                    ans -= 1
            if c == "B":
                ans += B[j+1]
                if 2*j-i < N and S[2*j-i] == "B":
                    ans -= 1
print(ans)