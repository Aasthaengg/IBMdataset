s = input()
F, T = False, True
ans = {(F, F): 'NA', (F, T): 'YYMM', (T, F): 'MMYY', (T, T): 'AMBIGUOUS'}
print(ans[1 <= int(s[:2]) <= 12, 1 <= int(s[2:]) <= 12])