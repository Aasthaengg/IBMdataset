N = int(input())
if N%2:
    print(0)
    exit()

ans = 0
r = 10
while r <= N:
    ans += N//r
    r *= 5
print(ans)