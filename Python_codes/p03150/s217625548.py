from itertools import product

S = input()

for i, j in product(range(len(S)), range(len(S))):
    if S[:i] + S[j:] == "keyence":
        print("YES")
        break
else:
    print("NO")
