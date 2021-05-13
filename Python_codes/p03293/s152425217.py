S = input()
T = input()
i = 0
while True:
    S = S[-1:]+S[:-1]
    if S == T:
        print("Yes")
        break
    else:
        i += 1
    if i == len(S):
        print("No")
        break