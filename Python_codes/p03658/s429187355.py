n, k = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]

ans = list(sorted(L))[::-1]
ans = sum(ans[0:k])
print(ans)