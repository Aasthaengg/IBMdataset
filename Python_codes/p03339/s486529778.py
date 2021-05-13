N = int(input())

S = input()

w = [0]*(N+1)
e = [0]*(N+1) 

for i in range(N):
    if S[i] == "W":
        w[i+1] = 1
    
    if S[i] == "E":
        e[i+1] = 1

for i in range(N):
    w[i+1] += w[i]
    e[i+1] += e[i]

ans = N
for i in range(1,N+1):
    d = w[i-1] + e[N]-e[i]
    ans = min(ans,d)

print(ans)
