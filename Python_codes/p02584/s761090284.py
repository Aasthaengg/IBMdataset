def resolve():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x // d > k:  # 最大長が0まで届くか
        print(x - k * d)
    elif (k - x // d) % 2 == 0:  # 0を反復横跳びする     偶数->X側、奇数->-X側
        print(x % d)
    else:
        print(d - x % d)
        
resolve()