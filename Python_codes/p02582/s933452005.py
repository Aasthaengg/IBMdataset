S = input()

ame = 0
if S[0] =="R":
    ame = 1
    if S[1] == "R":
        ame = 2
        if S[2] == "R":
            ame = 3
else:
    if S[1] == "R":
        ame = 1
        if S[2] == "R":
            ame = 2
    elif S[2] == "R":
        ame = 1
print(ame)
