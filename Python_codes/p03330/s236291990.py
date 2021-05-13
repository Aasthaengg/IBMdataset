n, c_cnt = map(int, input().split())
d = [list(map(int, input().split())) for i in range(c_cnt)]
c = [list(map(int, input().split())) for i in range(n)]

def solve():
    ans0 = []
    ans1 = []
    ans2 = []
    for col in range(1, c_cnt + 1):
        res = 0
        for i in range(n):
            for j in range(n):
                if (i + j) % 3 == 0:
                    res += d[c[i][j] - 1][col - 1]
        ans0.append(res)

    for col in range(1, c_cnt + 1):
        res = 0
        for i in range(n):
            for j in range(n):
                if (i + j) % 3 == 1:
                    res += d[c[i][j] - 1][col - 1]
        ans1.append(res)

    for col in range(1, c_cnt + 1):
        res = 0
        for i in range(n):
            for j in range(n):
                if (i + j) % 3 == 2:
                    res += d[c[i][j] - 1][col - 1]
        ans2.append(res)
        
    return ans0, ans1, ans2

res = 10 ** 18
ans0, ans1, ans2 = solve()
for i0, num0 in enumerate(ans0):
    for i1, num1 in enumerate(ans1): 
        for i2, num2 in enumerate(ans2):
            if i0 != i1 and i1 != i2 and i2 != i0:
                res = min(num0 + num1 + num2, res)
print(res)