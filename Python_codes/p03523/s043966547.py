s = input()

if s.replace("A", "") == "KIHBR":
    b1 = bool(s == "AKIHBR")
    b2 = bool(s == "KIHABR")
    b3 = bool(s == "KIHBAR")
    b4 = bool(s == "KIHBRA")
    b5 = bool(s == "AKIHABR")
    b6 = bool(s == "AKIHBAR")
    b7 = bool(s == "AKIHBRA")
    b8 = bool(s == "AKIHABAR")
    b9 = bool(s == "AKIHABRA")
    b10 = bool(s == "AKIHBARA")
    b11 = bool(s == "KIHABARA")
    b12 = bool(s == "AKIHABARA")
    B1 = b1 or b2 or b3 or b4
    B2 = b5 or b6 or b7 or b8
    B3 = b9 or b10 or b11 or b12
    if B1 or B2 or B3 or s == "KIHBR":
        print("YES")
        exit()
print("NO")