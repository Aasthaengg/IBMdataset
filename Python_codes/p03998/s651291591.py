SA = list(input())
SB = list(input())
SC = list(input())
turn = "a"
for i in range(300):
    if turn == "a":
        if not SA:
            print("A")
            exit()
        turn = SA[0]
        SA.pop(0)
    elif turn == "b":
        if not SB:
            print("B")
            exit()
        turn = SB[0]
        SB.pop(0)
    else:
        if not SC:
            print("C")
            exit()
        turn = SC[0]
        SC.pop(0)