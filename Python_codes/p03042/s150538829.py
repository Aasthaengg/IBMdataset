S = int(input())
S1, S2 = S // 100, S % 100

YYMM = (1 <= S2 and S2 <= 12)
MMYY = (1 <= S1 and S1 <= 12)

if YYMM and MMYY:
    print("AMBIGUOUS")
elif YYMM:
    print("YYMM")
elif MMYY:
    print("MMYY")
else:
    print("NA")