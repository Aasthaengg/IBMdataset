S = input()

heads = int(S[:2])
tails = int(S[2:])


def is_month(n):
    return n >= 1 and n <= 12


if is_month(heads) and (not is_month(tails)):
    print("MMYY")
elif (not is_month(heads)) and (not is_month(tails)):
    print("NA")
elif (not is_month(heads)) and is_month(tails):
    print("YYMM")
else:
    print("AMBIGUOUS")
