N = int(input())
V = sorted(list(map(int,input().split())))

ans = V[0]
for v in V[1:]:
    ans = (ans + v) / 2
print(ans)