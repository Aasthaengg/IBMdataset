S = input()
N = len(S)
keyence="keyence"

for i in range(N-1):
    for j in range(i,N):
        try_str = S[:i] + S[j:]
        if try_str == keyence:
            print("YES")
            exit()
print("NO")