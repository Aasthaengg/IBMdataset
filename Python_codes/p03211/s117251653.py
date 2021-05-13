S = input()
ans = 10000
for i in range(len(S)-2):
    tmp = abs(753-int(S[i:i+3]))
    if tmp < ans:
        ans = tmp
print(ans)