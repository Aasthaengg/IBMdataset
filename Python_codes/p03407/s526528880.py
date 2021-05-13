coin_a, coin_b, coin_c = [int(a) for a in input().split()]

coin_total = coin_a + coin_b

if coin_total >= coin_c:
    print("Yes")
else:
    print("No")