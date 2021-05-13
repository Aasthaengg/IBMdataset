N = int(input())
p = list(map(int, input().split()))

ans = 0

for i in range(N-1):
    if p[i] == i+1:
        # swap
        temp = p[i]
        p[i] = p[i+1]
        p[i+1] = temp
        ans += 1
if p[-1] == N:
    ans += 1
print(ans)