n, a, b = map(int,input().split())

if b < a:
    print(0)
    exit()
if (n == 1) & (b != a):
    print(0)
    exit()

ans = (b*(n-1)+a) - (a*(n-1)+b) + 1
print(ans)