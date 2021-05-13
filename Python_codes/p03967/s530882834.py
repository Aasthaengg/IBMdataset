S = input()
t = 0
p = 0
for s in S:
    if s == "g":
        if t > 0: #パーを出す
            t -= 1
            p += 1
            continue
        else:
            t += 1 #グーを出す
    else:
        if t > 0: #パーを出す
            t -= 1
        else: #グーを出す
            p -= 1
            t += 1
print(p)
