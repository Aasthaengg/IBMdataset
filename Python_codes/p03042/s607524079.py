S = input()
head = S[:2]
tail = S[2:]

MMYY = False
YYMM = False

if 1 <= int(head) <= 12:
    MMYY = True
if 1 <= int(tail) <= 12:
    YYMM = True

if MMYY and YYMM:
    print("AMBIGUOUS")
elif MMYY:
    print("MMYY")
elif YYMM:
    print("YYMM")
else:
    print("NA")

