S = str(input())

price = 700
count = 0

for i in S:
    if i == "o":
        count += 1

print("{}".format(price+count*100))