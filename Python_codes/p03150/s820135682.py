S = input()

def range_strip(S, i, j):
    return S[:i] + S[j:]

for i in range(len(S)):
    for j in range(i, len(S)):
        if range_strip(S,i,j) == "keyence":
            print("YES")
            exit(0)
print("NO")