s = input()
ans = {(False, False): 'NA', (False, True): 'YYMM', (True, False): 'MMYY', (True, True): 'AMBIGUOUS'}
print(ans[1 <= int(s[:2]) <= 12, 1 <= int(s[2:]) <= 12])