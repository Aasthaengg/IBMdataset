S = input()
N = len(S)
ans = 0
for i in range(N):
    for j in range(i+1):
        ans += int(S[N-i-1]) * 10 ** j * 2 ** (N-min(i+1, j+2))
print(ans)