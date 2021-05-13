S = input()

ans = 10**9
for i in range(len(S) - 2):
    x = S[i:i+3]
    now = abs(int(x) - 753)
    ans = min(ans, now)
print(ans)