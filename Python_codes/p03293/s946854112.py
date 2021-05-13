S = input()
T = input()
S = S + S

for i in range(len(T)):
    if S[i:i+len(T)] == T:
        print('Yes')
        exit()
print('No')