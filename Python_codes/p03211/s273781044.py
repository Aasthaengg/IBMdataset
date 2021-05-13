S = input()
ans = 1000
for i in range(len(S)-2):
    x = int(S[i:i+3])
    dif = abs(753 - x)
    ans = min(dif, ans)
print(ans)