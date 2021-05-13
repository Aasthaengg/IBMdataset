s = str(input())
count = 0

if s[0] == "o":
    count += 1

if s[1] == "o":
    count += 1

if s[2] == "o":
    count += 1

price = 700 + 100 * count
print(price)
