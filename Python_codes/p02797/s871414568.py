N, K, S = map(int, input().split())

str_S = str(S)
str_S1 = str(S+1)
ans = []
for _ in range(K):
    ans.append(str_S)
for _ in range(N-K):
    if S != 1000000000:
        ans.append(str_S1)
    else:
        ans.append('1')
print(' '.join(ans))
