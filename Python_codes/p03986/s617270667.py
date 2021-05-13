x = input()

ans = 0
stock = 0

for i in range(len(x)):
    if x[i] == 'S':
        stock += 1
    elif stock > 0:
        stock -= 1
    else:
        ans += 1

print(ans+stock)
