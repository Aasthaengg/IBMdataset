N = int(input())
p = [int(i) for i in input().split()]
ans = 0

for i in range(N-1):
    if p[i] == i + 1 and p[i+1] == i+2:
        p[i], p[i+1] = p[i+1], p[i]
        ans += 1
for i in range(N-1):
    if p[i] == i + 1:
        p[i], p[i+1] = p[i+1], p[i]
        ans += 1
if p[N - 1] == N:
    p[N-2], p[N-1] = p[N-1], p[N-2]
    ans += 1
print(ans)
