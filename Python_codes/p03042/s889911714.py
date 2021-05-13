S = int(input())

YYMM = 0
MMYY = 0

if S % 100 >= 1 and S % 100 <= 12:
    YYMM = 1

if S // 100 >= 1 and S // 100 <= 12:
    MMYY = 1

if YYMM == 0 and MMYY == 0:
    print('NA')
elif YYMM == 0 and MMYY == 1:
    print('MMYY')
elif YYMM == 1 and MMYY == 0:
    print('YYMM')
else:
    print('AMBIGUOUS')
