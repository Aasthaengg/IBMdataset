n = int(input())
p = [int(input()) for i in range(n)]

q = [0 for _ in range(n)]
for i in range(n):
    q[p[i]-1] = i
q.append(-1)

ans = 0
count = 1
for i in range(1, n+1):
    if q[i-1] < q[i]:
        count += 1
    else:
        ans = max(ans, count)
        count = 1

print(n-ans)