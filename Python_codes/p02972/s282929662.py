N, *A = map(int, open(0).read().split())

x = [0] * (N + 1)
ans = []
for i in reversed(range(1, N + 1)):
    if sum(x[i::i]) % 2 != A[i - 1]:
        x[i] += 1
        ans.append(i)

print(len(ans))
if ans:
    print(*ans)

