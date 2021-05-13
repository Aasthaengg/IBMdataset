N = int(input())
S = [input() for _ in range(3)]
ans = 0
for i in range(N):
    char = set()
    for j in range(3):
        char.add(S[j][i])
    ans += len(char) - 1
print(ans)