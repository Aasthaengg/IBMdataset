sa = str(input())
sb = str(input())
sc = str(input())

sa_len = len(sa)
sb_len = len(sb)
sc_len = len(sc)

sa_turn = 1#順番をきめてる
sb_turn = 0
sc_turn = 0

sa_pl = 0#今何個目を参照しているか
sb_pl = 0
sc_pl = 0






while True:
    if sa_turn == 1:
        if sa_len == sa_pl:
            print("A")
            break
        elif sa[sa_pl] == "a":
            sa_pl += 1
        elif sa[sa_pl] == "b":
            sa_turn = 0
            sb_turn = 1
            sa_pl +=1
        elif sa[sa_pl] == "c":
            sa_turn = 0
            sc_turn = 1
            sa_pl +=1
    
    elif sb_turn == 1:
        if sb_len == sb_pl:
            print("B")
            break
        elif sb[sb_pl] == "b":
            sb_pl += 1
        elif sb[sb_pl] == "a":
            sb_turn = 0
            sa_turn = 1
            sb_pl +=1

        elif sb[sb_pl] == "c":
            sb_turn = 0
            sc_turn = 1
            sb_pl +=1
    
    elif sc_turn == 1:
        if sc_len == sc_pl:
            print("C")
            break
        elif sc[sc_pl] == "c":
            sc_pl += 1
        elif sc[sc_pl] == "b":
            sc_turn = 0
            sb_turn = 1
            sc_pl +=1
        elif sc[sc_pl] == "a":
            sc_turn = 0
            sa_turn = 1
            sc_pl +=1