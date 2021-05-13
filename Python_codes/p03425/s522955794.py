N = int(input())
S = [input() for _ in range(N)]
res = [0] * 5
ini = 'MARCH'
for i in range(N):
    for j in range(5):
        if S[i][0] == ini[j]:
            res[j] += 1

ans = 0
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            ans += res[i]*res[j]*res[k]
print(ans)