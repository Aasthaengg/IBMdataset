n = int(input())
a = [int(_) for _ in input().split()]
dis = [0] * (n+1)
dis[0] = abs(a[0])
for i in range(1, n):
    dis[i] = abs(a[i] - a[i-1])
dis[n] = abs(a[n-1])
#print(dis)

total = 0
for i in dis:
    total += abs(i)
#print(total)

ans = [0] * n
ans[0] = total - (dis[0] + dis[1]) + abs(a[1])
for i in range(1, n-1):
    ans[i] = total - (dis[i] + dis[i+1]) + abs(a[i+1] - a[i-1])
ans[n-1] = total - (dis[n-1] + dis[n]) + abs(a[n-2])
#print(ans)
for i in ans:
    print(i)