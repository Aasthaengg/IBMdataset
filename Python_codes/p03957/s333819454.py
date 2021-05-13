S = input()
N = len(S)
for i in range(N):
    for j in range(i, N):
        if S[i] == "C" and S[j] == "F":
            print("Yes")
            exit()
print("No")