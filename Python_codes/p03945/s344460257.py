S = input()
N = len(S)
now = S[0]
ans = 0
for i in range(N-1):
    if S[i+1] != now:
        now = S[i+1]
        ans += 1
print(ans)