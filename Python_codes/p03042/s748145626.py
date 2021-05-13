S = str(input())
front = int(S[:2])
back = int(S[2:])
S_list = list(S)

if front > 12 or front == 0:
    if 0 < back <= 12 :
        print("YYMM")
    else:
        print("NA")
elif front <= 12 or front == 0:
    if 0 < back <= 12: 
        print("AMBIGUOUS")
    else:
        print("MMYY")