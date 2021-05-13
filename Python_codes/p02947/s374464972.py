N = int(input())
d = {}
for i in range(N):
    s = list(map(str, input()))
    s.sort()
    s = "".join(s)
    d[s] = d[s] + 1 if s in d else 1
ans = 0
for i in d.values():
    ans += i * (i-1) // 2
print(ans)
