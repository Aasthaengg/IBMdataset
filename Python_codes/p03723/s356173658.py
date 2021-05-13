a, b, c = map(int, input().split())

ans = 0
while (a % 2 == 0) & (b % 2 == 0) & (c % 2 == 0):
    a, b, c = (b + c) // 2, (c + a) // 2, (a + b) // 2
    ans += 1
    if ans>1000000:
        ans = -1
        break
print(ans)
