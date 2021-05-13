S = input()
T = "keyence"
for i in range(len(S)):
    for j in range(len(S)):
        if S[:i] + S[j:] == T:
            print('YES')
            exit()
print('NO')
