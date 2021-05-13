S = list(input())
S = [int(x) for x in S]

ans = float('inf')
target = 753
for i in range(len(S)-2):
    num = S[i] * 100 + S[i+1] * 10 + S[i+2] * 1
    diff = abs(target - num)
    ans = min(ans, diff)

print(ans)