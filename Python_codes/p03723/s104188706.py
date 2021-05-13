a, b, c = map(int, input().split())

ans = 0

while True:
    if ans > 999999:
        print(-1)
        break
    elif a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        print(ans)
        break
    n_a = b/2 + c/2
    n_b = a/2 + c/2    
    n_c = a/2 + b/2
    a = n_a
    b = n_b
    c = n_c
    ans += 1
