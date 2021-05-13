S = input()
C = 0
bw = S[0]
for i in range(1, len(S)):
    if bw != S[i]:
        C += 1
        bw = S[i]
print(C)