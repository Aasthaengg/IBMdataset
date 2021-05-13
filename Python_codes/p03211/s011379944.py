S = input()
n = len(S)
ans = 10**9
for i in range(n - 2):
    tmp = int(S[i:i + 3])
    diff = abs(753 - tmp)
    if diff < ans:
        ans = diff
print(ans)
