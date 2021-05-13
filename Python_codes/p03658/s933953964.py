n, k = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
ans = sum(L[-k:])
print(ans)