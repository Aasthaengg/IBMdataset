s = input()
for bit in range(1 << 3):
    tmp = int(s[0])
    sign = []
    for i in range(3):
        if bit & (1 << i):
            tmp += int(s[i+1])
            sign.append("+")
        else:
            tmp -= int(s[i+1])
            sign.append("-")
    
    if tmp == 7:
        print(s[0] + sign[0] + s[1] + sign[1] + s[2] + sign[2] + s[3] + "=7")
        exit()