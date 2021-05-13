S = input()
ans = 0
for i in range(len(S)):
    a = i
    k = 0
    while S[a] == 'A' or S[a] == 'C' or S[a] == 'G' or S[a] == 'T':
        k += 1
        a += 1
        if a == len(S):
            break
    ans = max(ans,k)
print(ans)