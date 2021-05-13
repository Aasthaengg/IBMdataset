r, d, x = map(int, input().split())
tem = x

for i in range(10):
    ans = r*tem - d
    tem = ans
    print(ans)