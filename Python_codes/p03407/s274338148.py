# Two Coins
print((lambda x: 'Yes' if x[0] + x[1] >= x[2] else 'No')(list(map(int, input().split()))))
