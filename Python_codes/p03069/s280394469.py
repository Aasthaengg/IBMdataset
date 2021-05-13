N = int(input())
S = "." + input() + "#"
B = [0]*(N+2)
W = [0]*(N+2)
b = 0
for k in range(N+2):
    if S[k] == "#":
        b += 1
    B[k] = b
w = 0
for k in range(N+1,-1,-1):
    if S[k] == ".":
        w += 1
    W[k] = w
ans = 10**10
for k in range(N+1):
    ans = min(ans,B[k]+W[k+1])
print(ans)
