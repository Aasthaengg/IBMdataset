import sys

S = input()
for i in range(len(S) + 1):
    for j in range(i, len(S) + 1):
        erased = S[:i] + S[j:]
        # print(i, j, erased)
        if erased == "keyence":
            print("YES")
            sys.exit()
print("NO")


