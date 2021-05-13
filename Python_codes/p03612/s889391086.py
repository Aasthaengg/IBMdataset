n = int(input())
*p, = map(int, input().split())
q = [True if p[i] != i+1 else False for i in range(n)] + [True]
ans = 0
for i in range(n):
    if not q[i]:
        ans += 1
        q[i] = q[i+1] = True
print(ans)
