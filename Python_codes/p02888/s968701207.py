import bisect

n = int(input())
ll = [int(w) for w in input().split()]
ll.sort()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans += bisect.bisect_left(ll, ll[i] + ll[j]) - (j + 1)

print(ans)
