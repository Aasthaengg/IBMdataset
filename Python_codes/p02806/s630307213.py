N = int(input())
ST = [input().split() for _ in range(N)]
X = input()
f = False
ans = 0
for s, t in ST:
    t = int(t)
    if f:
        ans += t
    if s == X:
        f = True
print(ans)