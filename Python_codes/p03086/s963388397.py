def is_ACGT(c):
    return c == "A" or c == "C" or c == "G" or c == "T"

S = input()

ans = 0
for i in range(len(S)):
    j = 0
    while i+j < len(S) and is_ACGT(S[i+j]):
        j += 1
    ans = max(ans, j)

print(ans)
