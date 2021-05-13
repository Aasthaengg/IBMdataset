A, B = map(int,input().split())
if B == 1:
    print(0)
else:
    num = A
    ans = 1
    while num < B:
        num += A-1
        ans += 1
    print(ans)