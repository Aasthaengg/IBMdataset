N = int(input())
TA = [tuple(map(int, input().split()))for _ in range(N)]
ans = TA[0]
for ta in TA[1:]:
    x = max((ans[0] + ta[0] - 1) // ta[0], (ans[1] + ta[1] - 1) // ta[1])
    ans = (x * ta[0], x * ta[1])
print(sum(ans))