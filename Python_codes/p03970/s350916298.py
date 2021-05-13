S = input()
ans = 0
for i in range(16):
    if S[i] != 'CODEFESTIVAL2016'[i]:
        ans += 1
print(ans)
