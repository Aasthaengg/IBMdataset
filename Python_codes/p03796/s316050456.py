def resolve():
    n = int(input())
    division_num = 10 ** 9 + 7
    
    ans = 1
    mod = 0
    for i in range(1, n + 1):
        ans *= i
        if ans > division_num:
            ans %= division_num
    
    print(ans)

resolve()