n, m = map(int, input().split())
gcd = m//n
while True:
    if m%gcd == 0:
        print(gcd)
        exit()
    gcd -= 1