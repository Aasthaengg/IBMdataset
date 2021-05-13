S = list(input())
N = len(S)
ans = 'NO'
for i in range(N):
    A = ''.join(S[:i] + S[N-7+i:])
    if A == 'keyence':
        ans = 'YES'
        break
print(ans)        