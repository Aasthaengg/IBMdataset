U = input()
S = [0]*len(U)
T = [0]*len(U)
for k in range(len(U)):
    if U[k] == "S":
        S[k] = 1
    else:
        T[k] = 1

for k in range(1,len(U)):
    S[k] += S[k-1]
    T[k] += T[k-1]
ans = 0
for k in range(len(U)):
    ans = max(ans,2*(T[k]-S[k]))
print(ans)
