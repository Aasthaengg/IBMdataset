N,K = map(int, input().split())
A = [int(a) for a in input().split()]

d = 50
L = [0]*d
for i in range(N):
    b = list(bin(A[i]))
    for j in range(2, len(b)):
        if b[j] == "1":
            L[len(b)-j-1] += 1

X0 = [0]*d
X1 = [0]*d
for i in range(d):
    X0[i] = 2**i*L[i]
    X1[i] = 2**i*(N-L[i])
    
ans = 0
    
Kb = list(bin(K))
for i in range(2, len(Kb)):
    if Kb[i] == "0":
        continue
    c = 0
    for j in range(2, len(Kb)):
        if j < i:
            if Kb[j] == "0":
                c += X0[len(Kb)-1-j]
            else:
                c += X1[len(Kb)-1-j]
        elif j == i:
            c += X0[len(Kb)-1-j]
        else:
            c += max(X0[len(Kb)-1-j], X1[len(Kb)-1-j])
    ans = max(ans, c)
    
for i in range(len(Kb)-2, d):
    ans += X0[i]
    
c = 0
for i in range(N):
    c += K^A[i]
    
ans = max(ans, c)
print(ans)