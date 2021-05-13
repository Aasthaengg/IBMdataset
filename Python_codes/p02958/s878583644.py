N = int(input())
p = list(map(int, input().split()))

sor_N = sorted(p)

cn = 0

for i in range(N):
    if p[i] != sor_N[i]:
        cn = cn + 1


if cn == 0 or cn == 2:
    print("YES")
else:
    print("NO")