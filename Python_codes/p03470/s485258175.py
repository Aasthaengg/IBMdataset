N = int(input())
d = []
for _ in range(N):
    x = int(input())
    d.append(x)
ans = len(set(d))
print(ans)
