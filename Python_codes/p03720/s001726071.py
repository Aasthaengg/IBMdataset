N, M = map(int, input().split())
ab = [[int(i) for i in input().split()] for i in range(M)]
ans = [0] * N

for a, b in ab:
    ans[a-1] += 1
    ans[b-1] += 1
for i in ans:
    print(i)