N = int(input())
d = sorted([int(input()) for i in range(N)])
ans = 1
for i in range(N-1):
    if d[i] < d[i+1]:
        ans += 1
print(ans)