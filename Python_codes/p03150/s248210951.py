S = input()
if S == "keyence":
    print("YES")
    exit()
for s in range(len(S)):
    for e in range(s, len(S)):
        string = S[:s] + S[e:]
        if string == "keyence":
            print("YES")
            exit()
print("NO")
