s = input()
a, b = int(s[:2]), int(s[2:])
r = ["AMBIGUOUS", "YYMM", "MMYY", "NA"]
print(r[(0 if (0 < b < 13) else 2) + (0 if (0 < a < 13) else 1)])