n = int(input())
V = tuple(map(int, input().split()))
V = sorted(V)
ans = V[0]
for v in V[1:]:
    ans = (ans+v)/2
print(ans)
