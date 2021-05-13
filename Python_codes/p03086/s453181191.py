S = input()
ans = 0
for i in range(len(S)):
    j = 0
    while i+j < len(S):
        if S[i+j:i+j+1] in ('A', 'C', 'T', 'G'):
            j += 1
        else:
            break
    ans = max(ans, j)

print(ans)
