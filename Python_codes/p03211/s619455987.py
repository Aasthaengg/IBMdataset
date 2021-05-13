S = input()
N = len(S)

ans = 1000
for i in range(N - 2):
    s = int(S[i:i + 3])
    ans = min(ans, abs(753 - s))
print(ans)