S = list(input())
n = len(S)

count = 0
if S[0] != "A" or not S[1].islower() or not S[-1].islower():
    print("WA")
else:
    count = 0
    for i in range(2, n-1):
        c = S[i]
        if c == "C":
            if count == 1:
                print("WA")
                break
            else:
                count = 1
        elif not c.islower():
            print("WA")
            break
    else:
        if count == 1:
            print("AC")
        else:
            print("WA")
