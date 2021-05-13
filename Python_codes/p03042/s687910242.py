s = input()
b1 = 1 <= int(s[:2]) <= 12
b2 = 1 <= int(s[2:]) <= 12
ans = ['NA', 'YYMM', 'MMYY', 'AMBIGUOUS']
print(ans[2*b1 + b2])