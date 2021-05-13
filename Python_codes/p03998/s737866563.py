Sa = list(input())[::-1]
Sb = list(input())[::-1]
Sc = list(input())[::-1]

next_turn = Sa.pop()


while True:
    if next_turn == "a":
        if not Sa:
            print("A")
            quit()
        next_turn = Sa.pop()
    elif next_turn == "b":
        if not Sb:
            print("B")
            quit()
        next_turn = Sb.pop()
    elif next_turn == "c":
        if not Sc:
            print("C")
            quit()
        next_turn = Sc.pop()
