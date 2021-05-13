import itertools
N = int(input())
S = [input() for _ in range(N)]
n = [0] * 5
for i in range(N):
    for j in range(5):
        if S[i][0] == ['M', 'A', 'R', 'C', 'H'][j]:
            n[j] += 1
ans = 0
for i in itertools.combinations(range(5), 3):
    ans += n[i[0]] * n[i[1]] * n[i[2]]
print(ans)
