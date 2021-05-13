S = input()
ans = 10**9

for i in range(len(S)):
    s = int(S[i:i+3])
    val = abs(753 - s)
    if val < ans:
        ans = val

print(ans)