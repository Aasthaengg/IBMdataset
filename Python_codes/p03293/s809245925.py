S = list(input())
T = list(input())
N = len(S)
ans = 'No'
for i in range(N):
    A = S[i:] + S[:i]
    if A == T:
        ans = 'Yes'
        break
print(ans)