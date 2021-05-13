S = input()
N = len(S)
for i in range(N):
    for j in range(i,N):
        if S[:i]+S[j:] == "keyence":
            print("YES")
            exit()
print("NO")
