N, M = map(int, input().split())

ans = {}
for i in range(8):
    ans[i] = []
for i in range(N):
    x, y, z = map(int, input().split())
    ans[0].append(x+y+z)
    ans[1].append(x+y-z)
    ans[2].append(x-y+z)
    ans[3].append(x-y-z)
    ans[4].append(-x+y+z)
    ans[5].append(-x+y-z)
    ans[6].append(-x-y+z)
    ans[7].append(-x-y-z)

max_ans = 0
for i in range(8):
    ans[i].sort(reverse=True)
    max_ans = max(max_ans, sum(ans[i][:M]))
print(max_ans)