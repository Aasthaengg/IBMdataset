s = input()
flg1 = 1 <= int(s[:2]) <= 12
flg2 = 1 <= int(s[2:]) <= 12
l = ["NA", "YYMM", "MMYY", "AMBIGUOUS"]
print(l[(flg1 << 1) + flg2])