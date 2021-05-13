S = list(input())
ans = 10**10
for i in range(0, len(S)-2):
    ans = min(abs(753-int(''.join(S[i:i+3]))), ans)
print(ans)
