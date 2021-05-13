S = input().strip()
r = 1000
for i in range(0, len(S)-2):
    r = min(r, abs(int(S[i:i+3])-753))
print(r)
