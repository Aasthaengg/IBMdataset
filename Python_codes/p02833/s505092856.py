n = int(input().rstrip())

if n % 2 == 1:
    print(0)
else:
    ans = 0
    for i in range(1, 30):#10^(18)<5^(29)*2 
        ans += n // (5**i * 2)
    print(ans)
