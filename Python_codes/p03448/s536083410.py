a_500 = int(input())
b_100 = int(input())
c_50 = int(input())
kadai = int(input())
sum_coins = []

for a in range(0, a_500+1, 1):
    for b in range(0, b_100+1, 1):
        for c in range(0, c_50+1, 1):
            sum_coins.append((500*a)+(100*b)+(50*c))
print(sum_coins.count(kadai))