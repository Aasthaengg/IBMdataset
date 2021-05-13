from bisect import bisect_right

n, x = map(int, input().split())
L = list(map(int, input().split()))
D = [0]
for i in range(n):
    D += [L[i] + D[i]]
ans = bisect_right(D, x)
print(ans)