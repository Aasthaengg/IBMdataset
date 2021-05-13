import bisect

n = int(input())
ll = list(map(int, input().split()))
ll.sort()

ans = 0
for i in range(n-2):
    e1 = ll[i]
    for j in range(i+1, n-1):
        e2 = ll[j]
        cnt = bisect.bisect_left(ll, e1+e2)
        cnt -= (j+1)
        ans += max(cnt,0)

print(ans)

