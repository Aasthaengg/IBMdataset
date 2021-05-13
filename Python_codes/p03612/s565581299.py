N = int(input())

p = list(map(int, input().split()))
ans = 0
for i in range(len(p)-1):
    if p[i] == i+1:
        p[i+1] = i+1
        ans += 1
if p[-1] == N: ans += 1
print(ans)