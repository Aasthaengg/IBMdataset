X, Y = map(int, input().split())

n = Y//X
ans = 0
while 2**ans <= n:
    ans += 1
print(ans)