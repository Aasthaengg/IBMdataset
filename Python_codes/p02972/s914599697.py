N, *A = map(int, open(0).read().split())

x = [0] * (N + 1)
ans = []
for i in reversed(range(1, N + 1)):
    tmp = 0
    for j in range(i, N + 1, i):
        tmp += x[j]

    if tmp % 2 != A[i - 1]:
        x[i] += 1
        ans.append(i)

print(len(ans))
if ans:
    print(*ans)

