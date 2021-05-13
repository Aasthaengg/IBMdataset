s = input()

c = 0

for i in range(3):
    if(s[i] == 'o'):
        c += 1

price = 700 + 100 * c

print(price)