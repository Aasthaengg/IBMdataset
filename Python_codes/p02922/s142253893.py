A, B = map(int, input().split())
if B == 1:
    print(0)
else:
    temp = 1
    ans = 0
    while True:
        if temp >= B:
            print(ans)
            break
        temp += A - 1
        ans += 1        