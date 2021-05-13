S = input()
ans = 1000
for i in range(len(S)-2):
    if abs(int(S[i:i+3])-753) < ans:
        ans = abs(int(S[i:i+3])-753)
print(ans)
