N,K = map(int, input().split())
S = list(input())

ans = 0

for i in range(1,N):
    if S[i-1]==S[i]:
        ans += 1

if ans + 2*K <= N-1:
    print(ans + 2*K)
else:
    print(N-1)
