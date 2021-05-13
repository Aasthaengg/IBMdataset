S = list(input())
if S[0] != "A":
    print("WA")
    exit()
else:
    idx = -1
    for i in range(2, len(S) - 1):
        if S[i] == "C":
            if idx == -1:
                idx = i
            else:
                print("WA")
                exit()
    if idx == -1:
        print("WA")
        exit()

    for i in range(len(S)):
        if i == 0 or i == idx:
            continue
        else:
            if S[i].islower() == False:
                print("WA")
                exit()
print("AC")
