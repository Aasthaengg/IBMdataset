S = list(input())
ans = 10 * 100
for i in range(len(S)-2):
    num = int("".join(S[i:i+3]))
    ans = min(abs(num-753), ans)
print(ans)