S = input()
ans = 0
tmp = S[0]
N = len(S)
if N == 1:
    print(0)
    exit()
for i in range(1, N):
    if i == N-1:
        ans += 1
    if S[i] != tmp:
        tmp = S[i]
        ans += 1
print(ans-1)