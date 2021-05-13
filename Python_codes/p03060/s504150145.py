N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

sm = list()
for a, b in zip(V, C):
    sm.append(a-b)

ans = 0

for a in sm:
    if a > 0:
        ans += a

print(ans)
