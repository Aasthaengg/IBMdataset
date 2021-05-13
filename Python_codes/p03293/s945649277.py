S = list(str(input()))
T = list(str(input()))

for i in range(len(S)):
    S.append(S[0])
    del S[0]
    if S == T:
        print("Yes")
        exit()

print("No")
