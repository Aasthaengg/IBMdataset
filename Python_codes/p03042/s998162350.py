s = input()
ans = [0,0]
if 1 <=  int(s[:2]) <= 12:
    ans[0] = 1
if 1 <= int(s[2:]) <= 12:
    ans[1] = 1
print([["NA","YYMM"],["MMYY","AMBIGUOUS"]][ans[0]][ans[1]])