N, M, *ab = map(int, open(0).read().split())
ans = [0] * N
for a, b in zip(*[iter(ab)] * 2):
    ans[a - 1] += 1
    ans[b - 1] -= 1
print("NO") if any(a % 2 for a in ans) else print("YES")
