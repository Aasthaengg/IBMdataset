N = int(input())

def solve(x):
    global res
    if x % 2 == 1:
        return res
    x = x // 2
    res += 1
    solve(x)

ans = []
for i in range(1, N+1):
    res = 0
    solve(i)
    ans.append([i, res])

ans = sorted(ans, key=lambda x:x[1], reverse=True)
print(ans[0][0])