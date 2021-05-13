S = input()

if S == "keyence":
    print("YES")
    exit()

for i in range(len(S)-1):
    for j in range(i+1, len(S)):
        if S[:i]+S[j:] == "keyence":
            print("YES")
            exit()

print("NO")