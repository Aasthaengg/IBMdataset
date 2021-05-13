N = int(input())
M,A,R,C,H = 0,0,0,0,0
for i in range(N):
    S = input()
    if S[0] == "M":
        M += 1
    elif S[0] == "A":
        A += 1
    elif S[0] == "R":
        R += 1
    elif S[0] == "C":
        C += 1
    elif S[0] == "H":
        H += 1
ans = 0
MARCH = [M,A,R,C,H]
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            ans += MARCH[i]*MARCH[j]*MARCH[k]
print(ans)