S = input()

ans = 999

for i in range(len(S)-2):
    num = int(S[i:i+3])
    if abs(num - 753) < ans:
        ans = abs(num-753)

print(ans)