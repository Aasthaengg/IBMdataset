S = input()
T = input()

ans = float('INF')
for i in range(len(S)-len(T) + 1):
    diff = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            diff += 1
    ans = min(ans, diff)
print(ans)