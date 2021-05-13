S = input()
L = len(S)
ACGT = ['A', 'C', 'G', 'T']
ans = 0

for i in range(L):
    for j in range(i, L):
        sub_S = S[i:j+1]
        if all([s in ACGT for s in sub_S]):
            if len(sub_S) > ans:
                ans = len(sub_S)

print(ans)
