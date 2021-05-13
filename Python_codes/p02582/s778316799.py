S = input()
length = len(S)
while True:
    R_l = "R" * length
    if R_l in S:
        print(length)
        break
    else:
        length -=1