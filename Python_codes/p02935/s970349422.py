N = int(input())
v = list(map(int, input().split()))
ans = min(v)
v.remove(min(v))
for i in range(N-1):
    ans = (ans + min(v)) /2
    v.remove(min(v))

print(ans)