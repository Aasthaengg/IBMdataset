SA = list(input())
SB = list(input())
SC = list(input())


card = SA.pop(0)
while True:

    if card == "a":
        if len(SA) == 0:
            print("A")
            break
        card = SA.pop(0)
    elif card == "b":
        if len(SB) == 0:
            print("B")
            break
        card = SB.pop(0)
    elif card == "c":
        if len(SC) == 0:
            print("C")
            break
        card = SC.pop(0)
