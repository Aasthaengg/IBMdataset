N, D = map(int, input().split())
ans = 0
while N > 0:
    N -= 2*D + 1
    ans += 1
print(ans)