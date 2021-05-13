n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

val = 0
ans = 0

for i in range(n):
    val = v[i] - c[i]
    if val > 0:
        ans += val
    else:
        pass
print(ans)