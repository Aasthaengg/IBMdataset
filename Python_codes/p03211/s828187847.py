S = input()

ans = 1000
for i in range(len(S)-2):
    t = abs(int(S[i:i+3])- 753)
    if t < ans:
        ans = t
print(ans)