S = input()
N = len(S)
A = [0] * (N+1)
C = [0] * (N+1)
X = [0] * (N+1)
Y = [0] * (N+1)

for i in range(N):
    A[i+1] = A[i] + (1 if S[i] == "A" else 0)
    X[i+1] = X[i] + (1 if S[i] == "?" else 0)
for i in range(N)[::-1]:
    C[i] = C[i+1] + (1 if S[i] == "C" else 0)
    Y[i] = Y[i+1] + (1 if S[i] == "?" else 0)

P = 10**9 + 7
POW = [1]
for i in range(2*N+10):
    POW.append(POW[-1]*3%P)
    
ans = 0
for i in range(N):
    if S[i] == "B" or S[i] == "?":
        a, x, c, y = A[i], X[i], C[i+1], Y[i+1]
        ans += a * c * POW[x+y]
        if x: ans += x * c * POW[x+y-1]
        if y: ans += a * y * POW[x+y-1]
        if x and y: ans += x * y * POW[x+y-2]
        ans %= P
print(ans)