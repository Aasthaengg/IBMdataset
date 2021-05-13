n = int(input())
N = 55556

memo = [1] * N
memo[0] = 0
memo[1] = 0

for i in range(2, N):
    if memo[i]:
        for j in range(2, N):
            if i * j >= N:
                break
            memo[i*j] = 0

ans = []
for i in range(2, N):
    if memo[i]:
        if i % 5 == 1:
            ans.append(str(i))

print(' '.join(ans[:n]))


