N = int(input())
a = list(map(int, input().split()))
ans = [0] * N

for i in range(N, 0, -1):
    j = 2*i - 1
    now = 0
    while j < N:
        now += ans[j]
        j += i
    if now % 2 != a[i-1]:
        ans[i-1] = 1

S = sum(ans)
print(S)
if S:
    print(*[i+1 for i in range(N) if ans[i]])

