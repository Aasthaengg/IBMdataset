S = input()
T = input()

N = len(S)
for i in range(N):
    S = S[N-1:] + S
    S = S[:N]
    if S == T:
        print("Yes")
        exit()

print("No")