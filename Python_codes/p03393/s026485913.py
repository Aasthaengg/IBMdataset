S = input()
alpha = [0] * 26
for s in S:
    alpha[ord(s) - 97] = 1

for i, value in enumerate(alpha):
    if value == 0:
        S = S + chr(i + 97)
        print(S)
        exit()

while len(S) > 1 or S[0] != 'z':
    idx = ord(S[-1]) - 97 + 1
    for i in range(idx, 26):
        if alpha[i] == 0:
            S = S[:-1] + chr(i + 97)
            print(S)
            exit()
    alpha[idx - 1] = 0
    S = S[:-1]

print(-1)
