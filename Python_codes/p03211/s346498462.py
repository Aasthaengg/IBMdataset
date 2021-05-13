S = input()

i = 0
ans = int(S)
while i < len(S)-2:
    num = int(S[i:i+3])
    i += 1
    ans = min(ans, abs(num-753))
print(ans)