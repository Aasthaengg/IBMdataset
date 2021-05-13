S = input()
ans = 0
count = 0
ACGT = ['A', 'C', 'G', 'T']
for i in range(len(S)):
    for j in range(i, len(S)):
        if all(ACGT.count(c) == 1 for c in S[i : j+1]):
            ans = max(ans, j-i+1)
print(ans)