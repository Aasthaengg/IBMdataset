num = input()
length, res = len(num), 0
big, small = "9", "1"

for dig_len in range(1, length + 1, 2):
    if int(big) < int(num):
        res += int(big) - int(small) + 1
        big += "99"
        small += "00"
    else:
        res += int(num) - int(small) + 1

print(res)
