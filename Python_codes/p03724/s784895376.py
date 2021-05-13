N, M = map(int, input().split())
Ans = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Ans[a] += 1
    Ans[b] += 1

for a in Ans:
    if a % 2 != 0:
        print('NO')
        exit()
print('YES')
