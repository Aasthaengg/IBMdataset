
n, k = [int(i) for i in input().split()]
ans = [1 for i in range(k)]
ans[-1] += n - sum(ans)
print(max(ans) - min(ans))
