n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
for i, ai in reversed(list(enumerate(a, 1))):
    s = sum(ans[j - 1] for j in range(i + i, n + 1, i))
    ans[i - 1] = (s + a[i - 1]) % 2
ans = list(map(lambda x: x[0], filter(lambda x: x[1] == 1, enumerate(ans, 1))))
print(len(ans))
print(*ans)