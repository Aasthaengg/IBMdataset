n,m = map(int, input().split())
x = [0] * m
for _ in range(n):
    a = list(map(int, input().split()))[1:]
    for ai in a:
        x[ai-1] += 1
ans = len([1 for i in range(m) if x[i] == n])
print(ans)