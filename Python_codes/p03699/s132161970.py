N = int(input())
ans = 0
S = []

for _ in range(N):
    si = int(input())
    ans += si
    if si % 10 != 0:
        S.append(si)

if ans % 10 != 0:
    print(ans)
else:
    if not S:
        print(0)
    else:
        ans -= min(S)
        print(ans)
