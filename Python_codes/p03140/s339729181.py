N = int(input())
S = [input() for _ in range(3)]
ans = 0
for i in range(N):
    ans += len(set([S[0][i], S[1][i], S[2][i]]))-1
print(ans)
