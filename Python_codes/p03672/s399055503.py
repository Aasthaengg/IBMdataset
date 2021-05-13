S = input()

ls = len(S)

while True:
    ls -= 1
    if ls % 2 == 1:
        continue
    leftS = S[0:ls//2]
    rightS = S[ls//2:ls]
    if leftS == rightS:
        print(ls)
        exit()

