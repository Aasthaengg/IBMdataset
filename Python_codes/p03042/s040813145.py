def solve(yy,mm):
    if 1<=yy<=12:
        if 1 <= mm <=12:
            return 'AMBIGUOUS'
        else:
            return 'MMYY'
    else:
        if 1<= mm <= 12:
            return 'YYMM'
        else:
            return "NA"


s = input()
yy = int(s[:2])
mm = int(s[2:])
print(solve(yy,mm))