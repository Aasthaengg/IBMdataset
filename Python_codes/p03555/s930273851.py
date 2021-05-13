C = [input() for i in range(2)]

if C[0][0] == C[1][2] and C[0][1] == C[1][1] and C[0][2] == C[1][0] and C[1][0] == C[0][2] and C[1][1] == C[0][1] and C[1][2] == C[0][0]:
    print("YES")
else:
    print("NO")