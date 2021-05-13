S = input()
Steam = 0
minecraft = 0
for i in range(len(S)):
    if S[i] == "+":
        minecraft += 1
    else:
        Steam += 1
L = minecraft * 1
P = Steam * -1
print(L + P)