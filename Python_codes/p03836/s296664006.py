sx, sy, tx, ty = map(int, input().split())


def inverse(line :str):
    ret = ""
    for c in line:
        if c == "U":
            ret += "D"
        elif c == "D":
            ret += "U"
        elif c == "R":
            ret += "L"
        else:
            ret += "R"
    
    return ret

# 1st loop
str1out = ""
for dx in range(tx - sx):
    str1out += "R"

for sy in range(ty - sy):
    str1out += "U"

str1in = inverse(str1out)

# 2nd loop
str2out = "DR" + str1out + "UL"
str2in = "UL" + str1in + "DR"
print(str1out + str1in + str2out + str2in)
