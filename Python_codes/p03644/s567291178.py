n = int(input())
ans = 1
while True:
    ans *= 2
    if ans > n:
        ans = ans // 2
        break
print(ans)